import streamlit as st

def landing_page():
    st.set_page_config(page_title="Wella.AI – Smart Diagnosis", layout="wide")

    st.markdown("""
    <style>
    .hero {
        background: linear-gradient(to right, #00b894, #00cec9);
        color: white;
        padding: 5rem 2rem;
        text-align: center;
        border-radius: 1rem;
        margin-bottom: 3rem;
    }
    .hero h1 {
        font-size: 3.5rem;
        margin-bottom: 1rem;
    }
    .hero p {
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .launch-button {
        background-color: white;
        color: #00b894;
        font-weight: bold;
        font-size: 1.1rem;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 0.5rem;
        cursor: pointer;
        text-decoration: none;
    }

    .section {
        padding: 2rem 1rem;
    }

    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
    }

    .feature-box {
        background: #f9f9f9;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        text-align: center;
    }

    .testimonial {
        background-color: #f1f1f1;
        padding: 2rem;
        border-radius: 1rem;
        font-style: italic;
        margin-top: 2rem;
    }

    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: gray;
        margin-top: 3rem;
    }
    </style>

    <div class="hero">
        <h1>Wella.AI – Smart Diagnosis Anytime, Anywhere</h1>
        <p>Empowering rural clinics with AI-powered medical diagnosis – even offline.</p>
        <a href="/?page=login" target="_self">
            <button class="launch-button">🚀 Launch Wella.AI</button>
        </a>
    </div>

    <div class="section">
        <h2 style="text-align:center;">💡 Key Features</h2>
        <div class="features-grid">
            <div class="feature-box">
                <h4>🧠 AI-Powered Diagnosis</h4>
                <p>Instant suggestions based on symptoms using machine intelligence.</p>
            </div>
            <div class="feature-box">
                <h4>📴 Offline Capability</h4>
                <p>Works without internet. Syncs when you’re back online.</p>
            </div>
            <div class="feature-box">
                <h4>👥 Role-Based Access</h4>
                <p>Admins, Doctors, and Nurses see only what they need.</p>
            </div>
            <div class="feature-box">
                <h4>🔐 Secure Storage</h4>
                <p>Encrypted data saved locally and synced to Supabase securely.</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2 style="text-align:center;">🗣️ What People Are Saying</h2>
        <div class="testimonial">
            “Wella.AI transformed our remote clinic. We can now treat more patients with confidence, even in disconnected areas.”  
            <br><br>– Dr. Grace Okoro, Rural Healthcare Coordinator
        </div>
    </div>

    <div class="footer">
        &copy; 2025 Wella.AI. All rights reserved.
    </div>
    """, unsafe_allow_html=True)
