1. Clone the repository
git clone https://github.com/kipkemoifred/pawait-chatbot-backend
cd pawait-chatbot-backend

2. Install dependencies
install python 3.10
pip install python-dotenv
pip install -q -U google-genai

3. Create a .env file
touch .env
add the following line
GEMINI_API_KEY=[your api key]

4. Run the server
fastapi dev main.py