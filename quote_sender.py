import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Replace with your own quotes or load from an external file
QUOTES = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "Act as if what you do makes a difference. It does. - William James",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "Do not wait; the time will never be 'just right.' Start where you stand. - Napoleon Hill",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Dream big and dare to fail. - Norman Vaughan",
    "It always seems impossible until it’s done. - Nelson Mandela",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "Keep your face always toward the sunshine, and shadows will fall behind you. - Walt Whitman",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
    "Turn your wounds into wisdom. - Oprah Winfrey",
    "If you want to lift yourself up, lift up someone else. - Booker T. Washington",
    "I can do all things through Christ who strengthens me. - Philippians 4:13",
    "Believe in yourself and all that you are. - Christian D. Larson",
    "The best way to predict the future is to create it. - Abraham Lincoln",
    "Don’t let yesterday take up too much of today. - Will Rogers",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "You are braver than you believe, stronger than you seem, and smarter than you think. - A.A. Milne",
    "With the new day comes new strength and new thoughts. - Eleanor Roosevelt",
    "Failure will never overtake me if my determination to succeed is strong enough. - Og Mandino",
    "We may encounter many defeats, but we must not be defeated. - Maya Angelou",
    "Your time is limited, don’t waste it living someone else’s life. - Steve Jobs",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "Don’t wish it were easier. Wish you were better. - Jim Rohn",
    "The man who has confidence in himself gains the confidence of others. - Hasidic Proverb",
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
    "You can’t cross the sea merely by standing and staring at the water. - Rabindranath Tagore",
    "A person who never made a mistake never tried anything new. - Albert Einstein",
    "Only put off until tomorrow what you are willing to die having left undone. - Pablo Picasso",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Setting goals is the first step in turning the invisible into the visible. - Tony Robbins",
    "Quality is not an act, it is a habit. - Aristotle",
    "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future. - Jeremiah 29:11",
    "If you genuinely want something, don’t wait for it—teach yourself to be impatient. - Gurbaksh Chahal",
    "All progress takes place outside the comfort zone. - Michael John Bobak",
    "Challenges are what make life interesting, and overcoming them is what makes life meaningful. - Joshua J. Marine",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "If you can dream it, you can achieve it. - Zig Ziglar",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "Everything you’ve ever wanted is on the other side of fear. - George Addair",
    "Whether you think you can or you think you can’t, you’re right. - Henry Ford",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "The best revenge is massive success. - Frank Sinatra",
    "Failure is simply the opportunity to begin again, this time more intelligently. - Henry Ford",
    "Don’t count the days, make the days count. - Muhammad Ali",
    "It’s not whether you get knocked down, it’s whether you get up. - Vince Lombardi",
    "Motivation is what gets you started. Habit is what keeps you going. - Jim Ryun",
    "Success is how high you bounce when you hit bottom. - George S. Patton",
    "Do what you feel in your heart to be right – for you’ll be criticized anyway. - Eleanor Roosevelt",
    "The Lord is my shepherd; I shall not want. - Psalm 23:1",
    "To see what is right and not do it is a lack of courage. - Confucius",
    "Even if you’re on the right track, you’ll get run over if you just sit there. - Will Rogers",
    "People who are crazy enough to think they can change the world are the ones who do. - Rob Siltanen",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "Action is the foundational key to all success. - Pablo Picasso",
    "Every moment is a fresh beginning. - T.S. Eliot",
    "Do one thing every day that scares you. - Eleanor Roosevelt",
    "Your passion is waiting for your courage to catch up. - Isabelle Lafleche",
    "Great things never come from comfort zones. - Anonymous",
    "What we achieve inwardly will change outer reality. - Plutarch",
    "Don’t let the fear of losing be greater than the excitement of winning. - Robert Kiyosaki",
    "The secret of getting ahead is getting started. - Mark Twain"
]

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Get credentials from environment variables
EMAIL = os.getenv("SMTP_EMAIL")  # Your email from environment variable
PASSWORD = os.getenv("SMTP_PASSWORD")  # Your app password from environment variable
RECIPIENT = os.getenv("SMTP_RECIPIENT")  # Recipient's email from environment variable

def send_email(quote):
    try:
        # Create the email message with MIME
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = RECIPIENT
        msg['Subject'] = "Your Daily Motivation"
        
        # HTML email body with styling
        message = f"""\
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; padding: 20px;">
                <div style="max-width: 600px; margin: auto; text-align: center; padding: 20px; background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                    <h1 style="color:rgb(92, 141, 232);">Good Morning Achiever!</h1>
                    <p style="font-size: 18px; color: #555;">Here’s your motivational quote for the day:</p>
                    <blockquote style="font-size: 24px; color: #555; font-style: italic;">
                        "{quote}"
                    </blockquote>
                    <p style="color: #777;">Stay positive and keep pushing forward!</p>
                    <hr style="border: 0; border-top: 1px solid #ddd; margin: 20px 0;">
                    <footer>
                        <p style="color: #888; font-size: 14px;">This email was automatically sent by your Daily Motivation Bot.</p>
                    </footer>
                </div>
            </body>
        </html>
        """
        
        # Attach the HTML message to the email
        msg.attach(MIMEText(message, 'html', 'utf-8'))
        
        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, RECIPIENT, msg.as_string())
            print("Email sent successfully.")

    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Choose a random quote
    daily_quote = random.choice(QUOTES)
    send_email(daily_quote)
