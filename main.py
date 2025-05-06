from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def portfolio():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>AB KAIUM – Portfolio</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to bottom, #f0f4ff, #e3eafc);
                color: #2c3e50;
                padding: 2rem;
                margin: 0;
            }
            header {
                background-color: #007bff;
                color: white;
                padding: 1rem 2rem;
                border-radius: 10px;
                margin-bottom: 2rem;
            }
            h1 {
                margin: 0;
                font-size: 2.5rem;
            }
            .links a {
                color: #fff;
                margin-right: 15px;
                text-decoration: none;
                font-weight: bold;
            }
            .links a:hover {
                text-decoration: underline;
            }
            section {
                background-color: white;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
            }
            h2 {
                color: #007bff;
            }
            ul {
                padding-left: 1.5rem;
            }
            a {
                color: #007bff;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>AB KAIUM</h1>
            <p>Email: <a href="mailto:akkaium33@gmail.com" style="color: #fff;">akkaium33@gmail.com</a></p>
            <p class="links">
                <a href="https://www.linkedin.com/in/ab-kaium/" target="_blank">LinkedIn</a>
                <a href="https://github.com/Qyum" target="_blank">GitHub</a>
                <a href="https://leetcode.com/Qyum/" target="_blank">LeetCode</a>
                <a href="https://www.fiverr.com/users/qyum_ai/manage_gigs?current_filter=active" target="_blank">Fiverr</a>
                <a href="https://www.upwork.com/freelancers/~0173f8e3cad7a922c6" target="_blank">Upwork</a>
            </p>
        </header>

        <section class="summary">
            <h2>Summary</h2>
            <p>
                6+ years of experience in AI-driven fraud detection, speech recognition, recommender systems, and chatbot development. Strong Python backend skills (Django, Flask), and expertise in deploying AI models. Proven leadership in deep learning, LLMs, and graph models. Proficient with TensorFlow, PyTorch, and cloud platforms like AWS and Azure. Electrical and Electronic Engineering background, passionate about scalable AI solutions and real-world problem-solving.
            </p>
        </section>

        <section>
            <h2>Experience</h2>
            <!-- Experience content unchanged -->
        </section>

        <section>
            <h2>Skills</h2>
            <!-- Skills content unchanged -->
        </section>

        <section>
            <h2>Education</h2>
            <!-- Education content unchanged -->
        </section>

        <section>
            <h2>Projects</h2>

            <h3>Forgery Detection System</h3>
            <p>
                Used EfficientNet with advanced preprocessing and augmentation to detect facial manipulation in images (80% accuracy).
                <a href="https://github.com/Qyum/forgery-detection" target="_blank">GitHub</a>
            </p>

            <h3>Medical AI Chatbot</h3>
            <p>
                Healthcare chatbot using LangChain, Pinecone, and OpenAI (92% satisfaction).
                <a href="https://github.com/Qyum/medical-ai-chatbot" target="_blank">GitHub</a>
            </p>

            <h3>Face & Text-to-Video Generator</h3>
            <p>
                Text-prompt video generation using Stable Diffusion and GANs.
                <a href="https://github.com/Qyum/face-text-to-video" target="_blank">GitHub</a>
            </p>

            <h3>Bangla Deep Speech Recognition</h3>
            <p>
                Developed end-to-end Bangla speech-to-text system using Bi-RNNs. Includes full pipeline for training, inference, and deployment.
                <a href="https://github.com/qyum/Bangla-deep-speech-Recognition" target="_blank">GitHub</a>
            </p>

            <h3>Document Detection and Skew Correction</h3>
            <p>
                Implemented document corner detection and skew correction pipeline to improve OCR results and image readability.
            </p>

            <h3>Generate Music Tune</h3>
            <p>
                Built an AI-based music generation tool using deep learning models trained on MIDI data.
            </p>

            <h3>PID-Based Autonomous Robot</h3>
            <p>
                Designed a robot controlled via PID algorithm for line following and obstacle avoidance using Arduino and sensors.
            </p>

            <h3>Autonomous Driving Application</h3>
            <p>
                Created a car detection system for autonomous driving using computer vision and deep learning techniques.
            </p>

            <h3>Deep Neural Network Applications</h3>
            <p>
                Collection of various DNN-based experiments including classification, regression, and generative tasks.
            </p>

        </section>
    </body>
    </html>
    """
