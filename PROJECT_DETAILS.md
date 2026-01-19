# Student Wellness Chatbot 🌱🤖

## 1. Introduction
The **Student Wellness Chatbot** is an AI-powered, emotion-aware web application developed as part of the **IBM SkillsBuild Internship**.  
The project focuses on supporting students in managing **stress, emotions, and mental well-being** using modern AI technologies combined with responsible and ethical design practices.

The application is designed to simulate a **supportive digital companion** that interacts with students in real time, identifies emotional states, and responds with calm, empathetic, and context-aware guidance.

---

## 2. Motivation Behind the Project
In the academic environment, students often face:
- High exam pressure  
- Academic workload stress  
- Emotional fatigue and anxiety  
- Limited access to immediate emotional support  

The motivation of this project is to:
- Provide a **safe and non-judgmental space** for students  
- Use AI responsibly to support emotional well-being  
- Demonstrate practical application of AI, NLP, and system design concepts  

---

## 3. Overall System Architecture
The Student Wellness Chatbot follows a **single-application, session-based architecture** implemented using Python and Streamlit.

The system consists of the following logical components:
- User Interface Layer  
- Mood Detection Engine  
- Hybrid AI Response Engine  
- Session State Manager  
- Visualization and Feedback Module  
- Security and Ethics Layer  

All components work together in real time to deliver a smooth and secure user experience.

---

## 4. Detailed Working of the System (Step-by-Step Flow)

1. The user interacts with the chatbot through a Streamlit-based chat interface  
2. User input text is captured and sent to the backend logic  
3. The **Mood Detection Engine** analyzes the input using keyword-based NLP rules  
4. The detected mood is mapped to an emotional category and intensity level  
5. The **Hybrid AI Response Engine** generates a suitable response  
6. If negative emotions are detected:
   - Calm breathing exercises are displayed  
   - Positive affirmations are shown  
7. Session data such as mood history and interaction count is updated  
8. Emotional trends are visualized using real-time charts  

All processing is done within the current session to maintain **privacy and data safety**.

---

## 5. User Interface Design
The user interface is designed using **Streamlit** with the following goals:
- Simplicity  
- Accessibility  
- Calm and supportive visual appearance  

UI features include:
- Chat-based interaction layout  
- Mode selection buttons (Exam Mode, Focus Mode, Vent Mode)  
- Status cards for mood, emotional intensity, and interactions  
- Real-time emotion trend chart  

Animations and visual feedback are added to improve user engagement without overwhelming the user.

---

## 6. Mood Detection Engine (Technical Explanation)
The Mood Detection Engine is a rule-based NLP component that:
- Converts user input to lowercase  
- Searches for predefined emotional keywords  
- Classifies the input into one of the following moods:
  - Happy  
  - Stressed  
  - Sad  
  - Angry  
  - Neutral  

Each mood is associated with a predefined **emotional intensity score (1–10)**, allowing the system to represent emotions quantitatively.

---

## 7. Hybrid AI Response Engine (Advanced Design)
The chatbot implements a **hybrid response architecture**, which is an important advanced feature of the project.

### 7.1 Rule-Based Response Layer
- Provides immediate responses based on detected mood  
- Ensures zero delay in user interaction  
- Acts as a fallback mechanism  

### 7.2 AI-Based Response Layer (OpenAI API)
- Generates natural, empathetic, and context-aware responses  
- Enhances conversational quality and realism  
- Includes timeout and exception handling  

If the AI service is unavailable, the system automatically switches to rule-based responses, ensuring **fault tolerance and reliability**.

---

## 8. Session State Management
Streamlit session state is used to manage:
- User messages  
- Current mood  
- Emotional intensity  
- Interaction count  
- Mood history  

This approach ensures:
- No permanent storage of user data  
- Privacy-first system behavior  
- Consistent state during a single session  

---

## 9. Emotion Tracking and Visualization
The system records emotional intensity values after each interaction.
These values are plotted using a **line chart** to show mood trends.

This feature:
- Helps users reflect on their emotional journey  
- Encourages self-awareness  
- Adds analytical depth to the application  

---

## 10. Calm Exercise and Coping Module
When negative emotions are detected, the system automatically activates a **calm exercise module**.

This module includes:
- Guided breathing exercises  
- Simple coping suggestions  
- Positive affirmations  

The design follows **human-centered AI principles**, prioritizing user comfort and emotional safety.

---

## 11. Security Implementation
Security is a key consideration in this project:
- API keys are stored securely using **Streamlit Secrets**  
- Sensitive configuration files are excluded from GitHub using `.gitignore`  
- No personal or sensitive data is stored permanently  

These practices align with **industry-standard secure development guidelines**.

---

## 12. Ethical and Responsible AI Design
The project strictly follows ethical AI principles:
- No medical diagnosis or treatment claims  
- Clear disclaimers included  
- Educational and emotional support purpose only  
- Alignment with IBM Responsible AI guidelines  

---

## 13. Technical Characteristics
- Real-time processing  
- Stateless session-based design  
- Secure and fault-tolerant AI integration  
- Modular and maintainable code structure  
- Privacy-first architecture  

---

## 14. Limitations
- Requires active internet connection  
- Depends on external AI API availability  
- Emotion detection is keyword-based, not deep-learning based  

---

## 15. Future Enhancements
Potential improvements include:
- Machine learning–based emotion classification  
- Persistent user profiles (with consent)  
- Multilingual support  
- Mobile-friendly UI enhancements  

---

## 16. Conclusion
The **Student Wellness Chatbot** is a comprehensive AI-based system that demonstrates how modern technologies can be combined with ethical and human-centered design to support student mental well-being.

The project reflects **practical AI implementation**, secure architecture, and responsible development practices suitable for both **academic evaluation and industry-level understanding**.

---

## Developer
**Gunjan Sanjay Mutkure**  
IBM SkillsBuild Internship Project
