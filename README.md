<<<<<<< HEAD
📘 SochGPT - Private LLM Project

🧭 Index
	1.	What is a Private LLM and Why I Built It
	2.	Technologies Used and Their Purpose
	3.	Steps to Run It on Your System
	4.	How It Can Be Improved and My Learnings

⸻

1. What is a Private LLM and Why I Built It

A Private LLM (Large Language Model) is basically your own personal ChatGPT that runs locally without sending any data to the cloud. It’s your private assistant that you can run safely on your laptop, which keeps your data secure and allows full customization.

I built this because I wanted to understand how systems like ChatGPT actually work under the hood, how data is processed, how it connects to models like Ollama, and how everything communicates between backend and frontend. It’s also useful for companies or developers who want AI tools but don’t want to share their data with public APIs.

Why it’s beneficial:
	•	100% privacy — nothing leaves your device.
	•	Full control — you can train or customize your model.
	•	Offline support — you don’t need internet to use it.
	•	Perfect learning project for understanding how LLMs work end-to-end.

How it works (simple flow):

[User Input] → [React Frontend] → [FastAPI Backend] → [LangChain Pipeline]
     ↓                                              ↓
[Ollama Model (Local)] ← [Chroma Database (Docs)] ← [Response Returned]

This means:
	1.	You type something in the UI (React app)
	2.	It sends your message to the FastAPI backend
	3.	Backend uses LangChain + Chroma to search your documents (RAG)
	4.	Ollama generates a reply locally
	5.	The response comes back to your chat screen (SochGPT)

⸻

2. Technologies Used and Why

FastAPI – This is the Python framework used to create the backend API. It helps send and receive data between frontend and the LLM.

LangChain – It helps connect different components of the LLM workflow like the model, embeddings, and document search. Basically, it’s the brain behind connecting all pieces together.

ChromaDB – This is a vector database that stores document embeddings. When you upload PDFs or text files, Chroma helps the system find relevant parts when you ask questions.

Ollama – This is the local model runner. It loads models like mistral, llama3, etc., on your device and generates responses privately without sending anything online.

React + Vite (Frontend) – The UI where the user chats with SochGPT. It’s lightweight, fast, and connects directly to the backend.

Tailwind CSS – Used to make the interface look clean and modern easily.

Vercel – Used for deploying a demo version of the frontend so people can see it live without needing the backend.

⸻

3. Steps to Run It on Your System

Step 1: Clone the project

git clone https://github.com/sumeetmj59/SochGPT.git
cd SochGPT

Step 2: Set up backend
Make sure you have Python 3.10+ and Ollama installed.

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ollama serve
uvicorn api:app --reload --host 127.0.0.1 --port 8000

Then open http://127.0.0.1:8000/healthz￼ — it should say { "ok": true }.

Step 3: Set up frontend

cd sil-ui
npm install
npm run dev

Then open http://localhost:3001￼

That’s it — your SochGPT is now running locally!

⸻

4. How It Can Be Improved and My Learnings

Future improvements:
	•	Add memory — make SochGPT remember the previous chats.
	•	Use APIs to fetch real-time data (like current news or stock prices).
	•	Improve UI design for better chat flow.

What I learned from this project:
	•	How local LLMs work with frameworks like LangChain.
	•	The role of embeddings and vector databases.
	•	How backend and frontend communicate using APIs.
	•	Handling errors, environment files, and project structure properly.

How I’ll use this in future projects:
	•	Build company-specific AI assistants that respect data privacy.
	•	Develop internal chat systems that run securely inside organizations.
	•	Use these learnings in roles like AI Developer, Data Engineer, or System Designer.

⸻

This document is meant to help anyone (including me) understand what a Private LLM is, how SochGPT works, and how it can be extended further. It’s my journey of learning how to build something that’s not just AI, but truly mine.
=======
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
>>>>>>> 3b7269f7 (Initialize project using Create React App)
