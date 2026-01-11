import sqlite3
import random
import re
from typing import Dict, Tuple
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self, db_path="support.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS support_tickets (
                ticket_id TEXT PRIMARY KEY,
                status TEXT,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
    
    def insert_ticket(self, ticket_id: str, description: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO support_tickets (ticket_id, status, description) VALUES (?, ?, ?)",
            (ticket_id, "Unresolved", description)
        )
        conn.commit()
        conn.close()
    
    def get_ticket_status(self, ticket_id: str) -> str:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM support_tickets WHERE ticket_id = ?", (ticket_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

class ClassifierAgent:
    def __init__(self):
        self.client = None
    
    def _get_openai_client(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not self.client and api_key and api_key.strip() != "":
            try:
                import openai
                self.client = openai.OpenAI(
                    api_key=api_key
                )
                print(f"✅ OpenAI client created successfully")
                return self.client
            except Exception as e:
                print(f"❌ Failed to create OpenAI client: {e}")
                self.client = None
        return self.client
    
    def classify(self, message: str) -> Dict:
        client = self._get_openai_client()
        if not client:
            raise Exception("OpenAI API key is required for classification")
            
        prompt = f"""You are a banking customer service classifier. Classify this message into EXACTLY ONE category based on PRIMARY INTENT:

POSITIVE_FEEDBACK: Customer is happy, satisfied, thanking, praising, or expressing gratitude
NEGATIVE_FEEDBACK: Customer is reporting NEW problems, issues, or complaints that need a support ticket
QUERY: Customer is asking about existing ticket status, requesting information, or checking on something (even if frustrated)

IMPORTANT: If message contains a ticket number or asks about ticket status, classify as QUERY regardless of tone.

Examples:
- "Thanks for helping me" → POSITIVE_FEEDBACK
- "My card is broken and not working" → NEGATIVE_FEEDBACK  
- "What's the status of ticket 123?" → QUERY
- "Why is ticket 456 still unresolved? I'm frustrated!" → QUERY
- "All my tickets are always unresolved, what about 789?" → QUERY

Message: "{message}"

Respond with ONLY the category name (POSITIVE_FEEDBACK, NEGATIVE_FEEDBACK, or QUERY):"""
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=20,
            temperature=0
        )
        result = response.choices[0].message.content.strip().upper()
        
        # Map to our format
        if "POSITIVE" in result:
            return {"classification": "positive_feedback", "using_openai": True}
        elif "NEGATIVE" in result:
            return {"classification": "negative_feedback", "using_openai": True}
        elif "QUERY" in result:
            return {"classification": "query", "using_openai": True}
        else:
            return {"classification": "negative_feedback", "using_openai": True}  # Default
    
    def _fallback_classify(self, message: str) -> str:
        message_lower = message.lower()
        
        # Strong negative indicators
        strong_negative = ["hate", "worst", "terrible", "awful", "crashes", "broken", "useless", "horrible", "sucks", "garbage"]
        # Strong positive indicators  
        positive_words = ["thank", "thanks", "great", "excellent", "good", "love", "amazing", "wonderful", "perfect", "smooth", "best", "always best", "experience"]
        # Problem indicators
        problem_words = ["problem", "issue", "error", "not working", "failed", "trouble", "complaint", "bad", "hasn't arrived", "delayed"]
        # Query indicators
        query_words = ["status", "check", "ticket", "what is", "how is", "update"]
        
        # Check for strong negative first
        if any(word in message_lower for word in strong_negative):
            return "negative_feedback"
            
        # Check for queries
        if any(word in message_lower for word in query_words) and any(word in message_lower for word in ["ticket", "status"]):
            return "query"
        
        # Check for strong positive indicators
        if any(word in message_lower for word in positive_words):
            return "positive_feedback"
            
        # Count remaining indicators
        negative_count = sum(1 for word in problem_words if word in message_lower)
        
        if negative_count > 0:
            return "negative_feedback"
        else:
            return "positive_feedback"  # Default to positive if unclear

class FeedbackHandlerAgent:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
    
    def handle_positive(self, customer_name: str = "Customer") -> str:
        return f"Thank you for your kind words, {customer_name}! We're delighted to assist you."
    
    def handle_negative(self, message: str) -> str:
        ticket_id = str(random.randint(100000, 999999))
        self.db_manager.insert_ticket(ticket_id, message)
        return f"We apologize for the inconvenience. A new ticket #{ticket_id} has been generated, and our team will follow up shortly."

class QueryHandlerAgent:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.client = None
    
    def _get_openai_client(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not self.client and api_key and api_key.strip() != "":
            try:
                import openai
                self.client = openai.OpenAI(api_key=api_key)
                return self.client
            except Exception as e:
                print(f"❌ Failed to create OpenAI client: {e}")
                self.client = None
        return self.client
    
    def get_ticket_details(self, ticket_id: str) -> Dict:
        conn = sqlite3.connect(self.db_manager.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT status, description, created_at FROM support_tickets WHERE ticket_id = ?", (ticket_id,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return {
                "status": result[0],
                "description": result[1],
                "created_at": result[2]
            }
        return None
    
    def handle_query(self, message: str, customer_name: str = "Customer") -> str:
        ticket_match = re.search(r'#?(\d{6})', message)
        if not ticket_match:
            return "Please provide a valid 6-digit ticket number so I can help you better."
        
        ticket_id = ticket_match.group(1)
        ticket_details = self.get_ticket_details(ticket_id)
        
        if not ticket_details:
            return f"I couldn't find ticket #{ticket_id} in our system. Please double-check the ticket number or contact support if you need assistance."
        
        # Use OpenAI to generate intelligent response
        client = self._get_openai_client()
        if client:
            try:
                prompt = f"""You are a helpful banking customer service agent. A customer named {customer_name} is asking about their support ticket.

Ticket Details:
- Ticket ID: #{ticket_id}
- Status: {ticket_details['status']}
- Original Issue: {ticket_details['description']}
- Created: {ticket_details['created_at']}

Customer Query: {message}

Provide a helpful, empathetic response that:
1. Acknowledges their concern
2. Explains the current status clearly
3. Shows understanding of their original issue
4. Offers next steps or timeline if appropriate
5. Maintains a professional but friendly tone

Keep response under 100 words."""

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()
            
            except Exception as e:
                print(f"❌ OpenAI API error: {e}")
        
        # Fallback response if OpenAI fails
        return f"Hi {customer_name}, your ticket #{ticket_id} regarding '{ticket_details['description']}' is currently {ticket_details['status'].lower()}. Our team is working on resolving this issue and will update you soon."

class MultiAgentSystem:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.classifier = ClassifierAgent()
        self.feedback_handler = FeedbackHandlerAgent(self.db_manager)
        self.query_handler = QueryHandlerAgent(self.db_manager)
        self.logs = []
    
    def process_message(self, message: str, customer_name: str = "Customer") -> Dict:
        classification_result = self.classifier.classify(message)
        classification = classification_result["classification"]
        using_openai = classification_result["using_openai"]
        
        if classification == "positive_feedback":
            response = self.feedback_handler.handle_positive(customer_name)
            agent_used = "Feedback Handler (Positive)"
        elif classification == "negative_feedback":
            response = self.feedback_handler.handle_negative(message)
            agent_used = "Feedback Handler (Negative)"
        elif classification == "query":
            response = self.query_handler.handle_query(message, customer_name)
            agent_used = "Query Handler"
        else:
            response = "I'm sorry, I couldn't understand your message. Please try again."
            agent_used = "Error Handler"
        
        log_entry = {
            "message": message,
            "classification": classification,
            "agent_used": agent_used,
            "response": response,
            "using_openai": using_openai
        }
        self.logs.append(log_entry)
        
        return log_entry
