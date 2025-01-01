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
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Dream big and dare to fail. - Norman Vaughan",
    "It always seems impossible until it’s done. - Nelson Mandela",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "Do not wait; the time will never be 'just right.' Start where you stand. - Napoleon Hill",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
    "I can do all things through Christ who strengthens me. - Philippians 4:13",
    "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future. - Jeremiah 29:11",
    "The Lord is my shepherd; I shall not want. - Psalm 23:1",
    "And we know that in all things God works for the good of those who love him. - Romans 8:28",
    "Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go. - Joshua 1:9",
    "Trust in the Lord with all your heart and lean not on your own understanding. - Proverbs 3:5-6",
    "As iron sharpens iron, so one person sharpens another. - Proverbs 27:17",
    "The pain you feel today will be the strength you feel tomorrow. - Anonymous",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "Quality is not an act, it is a habit. - Aristotle",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
    "You don’t have to be great to start, but you have to start to be great. - Zig Ziglar",
    "Do not be afraid of growing slowly; be afraid only of standing still. - Indian Proverb",
    "A journey of a thousand miles begins with a single step. - Lao Tzu",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "Don’t let yesterday take up too much of today. - Will Rogers",
    "If you stand straight, do not fear a crooked shadow. - Indian Proverb",
    "An ounce of practice is worth more than tons of preaching. - Mahatma Gandhi",
    "When the character of a man is not clear to you, look at his friends. - Indian Proverb",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Be like the lotus: trust in the light, grow through the dirt, believe in new beginnings. - Indian Proverb",
    "Faith is taking the first step even when you don’t see the whole staircase. - Martin Luther King Jr.",
    "He who kneels before God can stand before anyone. - Anonymous",
    "God is our refuge and strength, an ever-present help in trouble. - Psalm 46:1",
    "A tree with strong roots laughs at storms. - Indian Proverb",
    "A bird sitting on a tree is never afraid of the branch breaking, because her trust is not in the branch but in her own wings. - Indian Proverb",
    "Blessed is the one who perseveres under trial because, having stood the test, that person will receive the crown of life. - James 1:12",
    "When you walk through the fire, you will not be burned; the flames will not set you ablaze. - Isaiah 43:2",
    "Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid. - John 14:27",
    "There is no shortcut for hard work that leads to effectiveness. - Indian Proverb",
    "Many are the plans in a person’s heart, but it is the Lord’s purpose that prevails. - Proverbs 19:21",
    "Patience is bitter, but its fruit is sweet. - Indian Proverb",
    "He who walks with the wise grows wise, but a companion of fools suffers harm. - Proverbs 13:20",
    "The best time to plant a tree was twenty years ago. The second best time is now. - Chinese Proverb",
    "It is not how much we do, but how much love we put into what we do that matters. - Mother Teresa",
    "Do not be quick with your mouth, do not be hasty in your heart to utter anything before God. God is in heaven, and you are on earth, so let your words be few. - Ecclesiastes 5:2",
    "What the superior man seeks is in himself; what the small man seeks is in others. - Confucius",
    "When the winds of change blow, some build walls while others build windmills. - Chinese Proverb",
    "Train up a child in the way he should go, and when he is old, he will not depart from it. - Proverbs 22:6",
    "A diamond is a piece of coal that handled stress exceptionally well. - Indian Proverb",
    "Faith does not make things easy, it makes them possible. - Luke 1:37",
    "You reap what you sow. - Galatians 6:7",
    "Wisdom is better than weapons of war. - Ecclesiastes 9:18",
    "He who has health has hope, and he who has hope has everything. - Indian Proverb",
    "Do not store up for yourselves treasures on earth, where moths and vermin destroy, and where thieves break in and steal. - Matthew 6:19",
    "As water reflects the face, so one’s life reflects the heart. - Proverbs 27:19",
    "When God gives you a new beginning, do not repeat the old mistakes. - Anonymous",
    "The early bird catches the worm, but the second mouse gets the cheese. - Indian Proverb",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill", 
    "The only way to do great work is to love what you do. - Steve Jobs", 
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt", 
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis", 
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe", 
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson", 
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman", 
    "It always seems impossible until it’s done. - Nelson Mandela", 
    "Don't limit your challenges. Challenge your limits. - Anonymous", 
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb", 
    "Success is how high you bounce when you hit bottom. - George S. Patton", 
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson", 
    "If you want to fly, you have to give up what weighs you down. - Roy T. Bennett", 
    "Dream big and dare to fail. - Norman Vaughan", 
    "The harder you work for something, the greater you’ll feel when you achieve it. - Anonymous", 
    "Don't wait. The time will never be just right. - Napoleon Hill", 
    "You miss 100% of the shots you don't take. - Wayne Gretzky", 
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon", 
    "You don’t have to be great to start, but you have to start to be great. - Zig Ziglar", 
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt", 
    "It does not matter how slowly you go, as long as you do not stop. - Confucius", 
    "Don’t be pushed by your problems. Be led by your dreams. - Ralph Waldo Emerson", 
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar", 
    "Believe you can and you’re halfway there. - Theodore Roosevelt", 
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson", 
    "Act as if what you do makes a difference. It does. - William James", 
    "Don’t count the days, make the days count. - Muhammad Ali", 
    "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett", 
    "Challenges are what make life interesting and overcoming them is what makes life meaningful. - Joshua J. Marine"
]


# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Get credentials from environment variables

EMAIL = os.getenv("EMAIL")  # Your email from environment variable
PASSWORD = os.getenv("PASSWORD")  # Your app password from environment variable

# Get multiple recipients from GitHub Secrets, split by commas
RECIPIENTS = os.getenv("RECIPIENT").split(",")  # This will split the string into a list of emails

def send_email(quote):
    try:
        # Create the email message with MIME
        msg = MIMEMultipart()
        msg['From'] = EMAIL
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
                        <p style="color: #888; font-size: 14px;">This email was automatically sent by your VetriBot Motivation.</p>
                        <p style="color: #888; font-size: 14px;"><br>MMM Info Tech</p>
                    </footer>
                </div>
            </body>
        </html>
        """

        # Attach the HTML message to the email
        msg.attach(MIMEText(message, 'html', 'utf-8'))
        
        # Send the email to the recipients (use Bcc for multiple recipients)
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            msg['To'] = RECIPIENTS[0]  # Only put the first recipient in 'To'
            msg['Bcc'] = ', '.join(RECIPIENTS)  # Add all recipients in the 'Bcc' field
            server.sendmail(EMAIL, RECIPIENTS, msg.as_string())
            print(f"Email sent successfully to {', '.join(RECIPIENTS)}.")

    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Choose a random quote
    daily_quote = random.choice(QUOTES)
    send_email(daily_quote)
