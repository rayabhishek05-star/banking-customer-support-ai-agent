# Banking Customer Support AI Agent - Project Introduction

## Applied Generative AI Specialization Capstone Project

### Problem Statement

Modern digital banking platforms handle high volumes of customer service interactions through fragmented systems that struggle to:
- Personalize responses effectively
- Provide timely status updates
- Scale efficiently with growing customer demands
- Parse user sentiment accurately

This project addresses these challenges by developing a **multi-agent GenAI system** tailored for banking customer support workflows, aiming to reduce manual effort, enhance customer satisfaction, and ensure timely responses.

## Project Objectives

Design and implement a multi-agent AI assistant that handles:
- **Classification** of incoming user messages into feedback (positive/negative) or queries
- **Personalized responses** based on classification and user sentiment  
- **Ticket tracking and updates** through integration with a support database

## Solution Architecture

### Multi-Agent System Design

#### 1. Classifier Agent
- **Input**: Unstructured user messages
- **Task**: Categorize messages into:
  - Positive Feedback
  - Negative Feedback  
  - Query
- **Technology**: OpenAI GPT-3.5-turbo with custom prompts
- **Implementation**: Uses intelligent prompt engineering to prioritize intent over sentiment

#### 2. Feedback Handler Agent
- **Positive Feedback**:
  - Generates personalized thank-you messages
  - Uses customer name for personalization
- **Negative Feedback**:
  - Generates unique 6-digit ticket numbers
  - Inserts tickets into SQLite database
  - Returns empathetic responses with ticket information

#### 3. Query Handler Agent (Enhanced)
- **Task**: Handle ticket status inquiries
- **Features**:
  - Extracts ticket numbers from messages
  - Retrieves full ticket context from database
  - **AI-Powered Responses**: Uses OpenAI GPT-3.5 to generate contextual, empathetic responses
  - Provides intelligent analysis of ticket status and next steps

## Technical Implementation

### Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Python 3.8+ | Core application logic |
| **AI Model** | OpenAI GPT-3.5-turbo | Classification and response generation |
| **Database** | SQLite | Ticket management and persistence |
| **Frontend** | Streamlit | Interactive web interface |
| **Environment** | python-dotenv | Configuration management |

### Key Python Functions & Classes

#### Core Classes
```python
class DatabaseManager:
    - init_db()              # Initialize SQLite database
    - insert_ticket()        # Create new support tickets
    - get_ticket_status()    # Retrieve ticket status
    - get_ticket_details()   # Get full ticket information

class ClassifierAgent:
    - classify()             # OpenAI-powered message classification
    - _get_openai_client()   # OpenAI client initialization
    - _fallback_classify()   # Backup classification logic

class FeedbackHandlerAgent:
    - handle_positive()      # Process positive feedback
    - handle_negative()      # Create tickets for complaints

class QueryHandlerAgent:
    - handle_query()         # AI-powered query responses
    - get_ticket_details()   # Retrieve comprehensive ticket data
    - _get_openai_client()   # OpenAI integration

class MultiAgentSystem:
    - process_message()      # Orchestrate agent workflow
```

#### Key Features Implemented

1. **Intelligent Classification**
   - Priority-based intent detection
   - Handles mixed sentiment queries
   - Robust fallback mechanisms

2. **AI-Enhanced Responses**
   - Context-aware ticket status explanations
   - Empathetic communication
   - Personalized customer interactions

3. **Database Integration**
   - Automatic ticket generation
   - Comprehensive ticket tracking
   - Real-time status updates

4. **Interactive Dashboard**
   - Real-time message processing
   - Classification confidence display
   - Processing logs and analytics
   - Support ticket database viewer

### Database Schema

```sql
CREATE TABLE support_tickets (
    ticket_id TEXT PRIMARY KEY,      -- 6-digit unique identifier
    status TEXT,                     -- Unresolved/Resolved
    description TEXT,                -- Customer complaint/feedback
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Sample Workflows

### Example 1: Positive Feedback
```
Input: "Thanks for resolving my credit card issue!"
→ ClassifierAgent → Positive Feedback
→ FeedbackHandlerAgent → Personalized thank-you
Output: "Thank you for your kind words, [CustomerName]! We're delighted to assist you."
```

### Example 2: Complaint Handling
```
Input: "My debit card replacement hasn't arrived yet"
→ ClassifierAgent → Negative Feedback
→ FeedbackHandlerAgent → Create ticket #123456
Output: "We apologize for the inconvenience. Ticket #123456 has been created."
```

### Example 3: Enhanced Query Response
```
Input: "Why is ticket 123456 still unresolved?"
→ ClassifierAgent → Query
→ QueryHandlerAgent → AI-generated contextual response
Output: "Hi [Customer], I understand your frustration about ticket #123456 regarding your debit card replacement. Your ticket is currently unresolved, but I can see it was created recently. Our team typically processes card replacement requests within 5-7 business days..."
```

## Key Enhancements Made

### 1. Improved Classification Logic
- **Intent-Priority Classification**: Prioritizes query intent over negative sentiment
- **Better Prompt Engineering**: Enhanced examples and clearer instructions
- **Robust Fallback**: Handles edge cases gracefully

### 2. AI-Powered Query Responses
- **Contextual Understanding**: Analyzes full ticket history
- **Empathetic Communication**: Acknowledges customer concerns
- **Actionable Information**: Provides next steps and timelines
- **Personalization**: Uses customer names and specific ticket details

### 3. Enhanced Database Operations
- **Full Ticket Context**: Retrieves complete ticket information
- **Comprehensive Logging**: Tracks all interactions and responses

## LLMOps Implementation

### Model Evaluation Features
- Classification accuracy tracking
- Response quality assessment
- Agent routing success rate monitoring
- Processing logs and analytics

### Streamlit UI Components
- **Interactive Dashboard**: Real-time message processing
- **Classification Display**: Shows confidence and reasoning
- **Database Viewer**: Browse all support tickets
- **Test Scenarios**: Quick-test buttons for each agent type
- **Logs & Analytics**: Processing history and performance metrics

## Security & Best Practices

- **API Key Management**: Environment variable configuration
- **Error Handling**: Graceful fallbacks for API failures
- **Input Validation**: Robust message parsing and validation
- **Database Security**: Parameterized queries to prevent injection

## Project Structure

```
├── app.py                 # Streamlit web interface
├── agents.py              # Multi-agent system implementation
├── intro.md               # This comprehensive project overview
├── README.md              # Setup and usage instructions
├── requirements.txt       # Python dependencies
├── test_agents.py         # Automated test suite
├── verify_setup.py        # System verification
├── support.db             # SQLite database (auto-generated)
└── .env                   # Environment configuration
```

## Success Metrics

- **Classification Accuracy**: Correctly routes messages to appropriate agents
- **Response Quality**: Generates contextual, helpful responses
- **Customer Satisfaction**: Provides empathetic, personalized interactions
- **System Reliability**: Handles errors gracefully with fallback mechanisms
- **Scalability**: Processes multiple concurrent requests efficiently

This implementation demonstrates a production-ready multi-agent AI system that combines the power of large language models with robust software engineering practices to solve real-world customer support challenges.
