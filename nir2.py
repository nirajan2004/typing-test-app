import streamlit as st
import time
import random

st.title("Typing Test 💡")

# ---------------- EASY ---------------- #

easy_paragraphs = [
    "Python is a simple and powerful programming language.",
    "Practice typing every day to improve your speed.",
    "Streamlit helps create web apps using only Python."
]

# ---------------- MEDIUM ---------------- #

medium_paragraphs =  [
    """Python is one of the most popular programming languages in the world.
It is widely used for web development, data science, and automation.
The language is beginner-friendly because of its simple syntax.
Many developers start their coding journey with Python.""",

    """Reading books regularly can improve vocabulary and communication skills.
It also helps people develop focus and creativity over time.
Even spending fifteen minutes a day reading can make a difference.
Books allow us to explore new ideas and perspectives.""",

    """Technology is changing the way people live and work every day.
Smartphones and the internet have connected billions of people globally.
New inventions continue to make communication faster and easier.
Learning technology skills is becoming more important for students.""",

    """Exercise is important for maintaining both physical and mental health.
Walking, jogging, or cycling can improve overall fitness levels.
Regular workouts help reduce stress and increase energy.
Healthy habits can lead to a happier lifestyle.""",

    """Streamlit allows developers to build web applications using Python only.
It is commonly used for machine learning and data science projects.
Creating apps with Streamlit is simple and beginner-friendly.
Many students use it to showcase their coding projects online.""",

    """Music has the power to influence emotions and improve mood instantly.
Different genres can help people relax, focus, or feel motivated.
Many people listen to music while studying or working.
Artists use music to express creativity and emotions.""",

    """Football is one of the most loved sports around the world.
Millions of fans watch international tournaments every year.
Teamwork and discipline are very important in the game.
Great players inspire young athletes to practice harder.""",

    """Typing speed improves with regular practice and consistency.
Using proper finger placement can increase accuracy significantly.
Online typing tests help users track their progress over time.
Patience and repetition are the keys to becoming faster.""",

    """Artificial intelligence is transforming industries across the globe.
AI systems can analyze data and make predictions quickly.
Many companies use AI to improve customer experiences.
The future of technology will heavily involve artificial intelligence.""",

    """Traveling allows people to experience different cultures and traditions.
It helps individuals learn more about the world around them.
Trying local food is often the best part of traveling.
Every journey creates memories that last for years.""",

    """A balanced diet is necessary for maintaining good health.
Fruits and vegetables provide essential vitamins and nutrients.
Drinking enough water keeps the body hydrated and active.
Healthy eating habits improve concentration and energy levels.""",

    """Learning to code requires patience, practice, and problem-solving skills.
Beginners often start with simple projects to build confidence.
Making mistakes is a natural part of the learning process.
Consistency is more important than studying for long hours once.""",

    """The internet has made learning accessible to people everywhere.
Students can watch lectures and read articles online for free.
Educational platforms provide courses on almost every subject.
Digital learning continues to grow rapidly each year.""",

    """Time management is an important skill for students and professionals.
Planning tasks in advance helps reduce stress and confusion.
Completing work on time improves productivity and discipline.
Small daily improvements lead to long-term success.""",

    """Nature provides peace and beauty that many people enjoy.
Forests, rivers, and mountains attract visitors from around the world.
Protecting the environment is necessary for future generations.
Simple actions like recycling can make a positive impact.""",

    """Gaming has become a major form of entertainment worldwide.
Some games improve problem-solving and teamwork abilities.
Professional esports competitions now attract millions of viewers.
Balance between gaming and studies is very important.""",

    """Morning routines can influence the productivity of an entire day.
Many successful people begin their day with exercise or meditation.
Good routines help create discipline and consistency in life.
Starting the day positively can improve motivation and focus.""",

    """Social media allows people to connect and share ideas instantly.
It helps businesses reach customers more effectively than before.
However, excessive usage can negatively affect concentration levels.
Using social media wisely is important for maintaining balance.""",

    """Space exploration has helped scientists understand the universe better.
Astronauts and satellites collect valuable information from space missions.
Many countries invest heavily in space research and technology.
Future missions may allow humans to travel farther into space.""",

    """Creativity is an important skill in art, science, and technology.
Creative thinking helps people solve problems in unique ways.
Practicing hobbies can improve imagination and confidence.
Innovation often begins with a simple creative idea."""
]

# ---------------- HARD ---------------- #

hard_paragraphs =  [
    """Python is considered one of the easiest programming languages for beginners to learn.
It has a clean and simple syntax that makes coding easier to understand.
Developers use Python for web development, automation, data science, and artificial intelligence.
Many popular companies rely on Python for building software and applications.
Students often choose Python because it helps them focus on logic instead of complex syntax.
Libraries such as NumPy and Pandas make data analysis more efficient.
Frameworks like Django and Flask are commonly used for creating websites.
Machine learning engineers frequently use Python for training AI models.
The language has a large community that provides tutorials and support online.
Open-source contributions have helped Python grow rapidly over the years.
Many schools and universities include Python in their curriculum today.
Learning Python can open doors to many career opportunities in technology.
Practice and consistency are important for mastering programming concepts.
Building small projects is one of the best ways to improve coding skills.
Debugging errors teaches developers how programs actually work internally.
Python continues to evolve with new features and improvements every year.
It is widely used across different industries around the world.
Beginners can start with simple programs before moving to advanced applications.
Understanding the basics well creates a strong programming foundation.
Coding regularly helps improve confidence and problem-solving abilities.""",

    """Exercise plays an important role in maintaining both physical and mental health.
People who exercise regularly often feel more energetic throughout the day.
Activities such as walking, running, and cycling improve cardiovascular fitness.
Strength training helps build muscles and improve body balance.
Regular workouts can reduce stress and improve mental well-being.
Doctors often recommend at least thirty minutes of daily exercise.
Stretching before and after exercise helps prevent injuries.
Healthy habits formed at a young age can benefit people for life.
Exercise also improves sleep quality and concentration levels.
Many athletes follow strict training routines to improve performance.
Playing sports teaches teamwork, discipline, and leadership skills.
Outdoor activities allow people to enjoy fresh air and nature.
Consistency is more important than working out intensely once in a while.
Fitness goals should be realistic and achievable for long-term success.
Combining exercise with a balanced diet produces better results.
People who stay active are less likely to face certain health problems.
Technology now allows individuals to track workouts using smart devices.
Even simple daily activities can contribute to better fitness.
Motivation and patience are necessary for maintaining healthy routines.
A healthy body often leads to a healthier and happier lifestyle.""",

    """Technology has transformed the way humans communicate and work.
The internet connects billions of people across different countries instantly.
Smartphones allow users to access information anytime and anywhere.
Online education platforms have made learning more accessible than ever before.
Businesses use technology to improve productivity and customer experiences.
Artificial intelligence is becoming increasingly important in modern industries.
Automation helps companies complete repetitive tasks more efficiently.
Social media platforms enable people to share ideas and opinions globally.
Cloud computing allows users to store and access data remotely.
Cybersecurity has become essential as digital threats continue to grow.
Developers constantly create new applications to solve everyday problems.
Virtual meetings have changed how organizations conduct business operations.
Technology also plays a major role in healthcare and scientific research.
Students use digital tools to improve learning and collaboration.
Innovation continues to shape the future of transportation and communication.
Many careers today require at least basic technology skills.
People must learn to balance technology usage responsibly.
Excessive screen time can negatively affect focus and health.
The future will likely bring even more advanced technological developments.
Understanding technology is becoming necessary in modern society.""",

    """Reading books is one of the best ways to gain knowledge and improve vocabulary.
Books allow readers to explore different ideas, cultures, and experiences.
Fiction stories help improve imagination and creativity among readers.
Non-fiction books provide valuable information about real-world topics.
Reading regularly can improve communication and writing skills significantly.
Many successful people develop habits of reading every single day.
Libraries provide quiet spaces where students can focus and learn peacefully.
Digital books have made reading more accessible through smartphones and tablets.
Reading before bedtime can help people relax and reduce stress levels.
Students who read often usually perform better in academics.
Books can inspire people to think differently and solve problems creatively.
Authors spend years developing stories and sharing their experiences with readers.
Historical books help us understand important events from the past.
Biographies teach valuable lessons from successful individuals.
Parents often encourage children to develop reading habits from a young age.
Reading also improves concentration and patience over time.
People can discover new hobbies and interests through books.
Book discussions allow readers to exchange ideas and opinions.
Consistent reading strengthens both memory and critical thinking abilities.
A single good book can positively influence someone's entire perspective on life.""",

    """Football is one of the most popular sports in the entire world.
Millions of fans watch football matches and tournaments every year.
The sport requires teamwork, discipline, and physical fitness.
Players train regularly to improve speed, stamina, and ball control.
Famous football clubs have supporters from many different countries.
International tournaments create excitement among fans worldwide.
Coaches develop strategies to help teams perform better during matches.
Practice sessions are important for improving passing and shooting skills.
Goalkeepers play a crucial role in defending the team from attacks.
Football matches teach players how to handle pressure and competition.
Young athletes often dream of becoming professional footballers someday.
Fans celebrate victories passionately and support teams during difficult times.
Sportsmanship and respect are important values in football.
Technology such as VAR has changed modern football decision-making.
Many legendary players inspire children to work harder and stay disciplined.
Football also creates opportunities for friendship and teamwork.
Clubs invest heavily in training facilities and youth academies.
The sport brings people together regardless of language or nationality.
Watching football can be entertaining and emotionally exciting.
Football continues to unite millions of people around the globe.""",

    """Traveling allows people to discover new places and cultures around the world.
Many travelers enjoy exploring famous landmarks and historical monuments.
Trying local food is often one of the most enjoyable travel experiences.
Traveling teaches people to adapt to different environments and situations.
It helps individuals understand traditions and lifestyles from other regions.
Photography allows travelers to capture memories from their journeys.
Planning trips carefully can save both time and money.
Traveling with friends or family often creates unforgettable experiences.
Some people travel for relaxation while others travel for adventure.
Nature destinations such as mountains and beaches attract millions of visitors.
Traveling can improve confidence and communication skills.
Learning a few local phrases can make interactions more enjoyable.
Tourism also supports local businesses and economies in many countries.
Long journeys sometimes teach patience and problem-solving abilities.
Modern transportation has made international travel easier than before.
Travel blogs and videos inspire many people to explore new destinations.
Respecting local customs is important while visiting foreign countries.
Travel experiences often remain memorable for many years.
Exploring different cultures broadens a person's perspective on life.
Every journey provides opportunities for learning and personal growth.""",

    """Artificial intelligence is rapidly changing industries across the world.
AI systems can analyze large amounts of data within seconds.
Companies use artificial intelligence to improve customer experiences and services.
Machine learning helps computers make predictions based on previous data.
Voice assistants are common examples of AI in everyday life.
Healthcare industries use AI to assist doctors in diagnosing diseases.
Self-driving vehicle technology depends heavily on artificial intelligence systems.
Businesses automate repetitive tasks to increase efficiency and reduce costs.
AI-powered recommendation systems are used on streaming platforms and online stores.
Researchers continue developing more advanced and accurate AI models.
Ethical concerns about artificial intelligence are widely discussed today.
People worry about privacy, job automation, and decision-making transparency.
Learning AI and data science skills can create valuable career opportunities.
Many universities now offer specialized courses in artificial intelligence.
Robotics combined with AI can perform dangerous tasks safely.
Governments are also investing heavily in AI research and innovation.
Technology experts believe AI will continue evolving rapidly in the future.
Human creativity and critical thinking remain important alongside automation.
Understanding AI basics is becoming useful for students and professionals alike.
Artificial intelligence will likely influence nearly every industry in coming years.""",

    """Time management is an essential skill for students and working professionals.
Proper planning helps people complete tasks more efficiently and on time.
Many successful individuals create schedules to organize their daily activities.
Prioritizing important tasks can reduce unnecessary stress and confusion.
Avoiding procrastination improves productivity and work quality significantly.
Students who manage time well often achieve better academic performance.
Short breaks between study sessions help maintain focus and energy.
Using calendars and reminder apps can improve organization skills.
Setting realistic goals makes it easier to track progress consistently.
Distractions such as excessive social media usage waste valuable time.
Completing small tasks early prevents work from accumulating later.
Good time management creates balance between studies, work, and relaxation.
Discipline and consistency are important for maintaining productive routines.
People who plan ahead are usually better prepared for challenges.
Learning to manage time effectively improves decision-making abilities.
Team projects often require coordination and proper scheduling.
Poor time management can lead to stress and missed opportunities.
Building productive habits takes patience and regular practice.
Efficient use of time increases confidence and overall satisfaction.
Strong time management skills contribute greatly to long-term success.""",

    """Nature provides beauty, peace, and resources essential for human survival.
Forests, rivers, mountains, and oceans support countless living organisms.
People often visit natural places to relax and reduce stress levels.
Fresh air and green environments improve both physical and mental health.
Animals depend on balanced ecosystems for food and shelter.
Human activities sometimes damage the environment through pollution and deforestation.
Climate change has become a major concern for scientists worldwide.
Recycling and reducing waste can help protect natural resources.
Planting trees contributes positively to the environment and air quality.
Governments and organizations promote awareness about environmental protection.
Renewable energy sources are becoming increasingly important today.
Students should learn about sustainability from an early age.
Wildlife conservation helps preserve endangered species for future generations.
Natural disasters remind humans about the power of nature.
Protecting water sources is essential for healthy communities.
Many photographers capture nature's beauty through stunning landscapes.
People can help the environment by making responsible daily choices.
Public parks provide spaces for exercise and outdoor activities.
Nature inspires artists, writers, and scientists in different ways.
Caring for the planet is a shared responsibility for everyone.""",

    """Gaming has become one of the largest entertainment industries in the world.
Many players enjoy video games for relaxation and social interaction.
Online multiplayer games allow people to connect with friends globally.
Esports competitions attract millions of viewers and professional players.
Strategy games often improve critical thinking and decision-making skills.
Some educational games help students learn subjects more interactively.
Game developers spend years creating detailed stories and gameplay systems.
Streaming platforms have made gaming content extremely popular online.
Parents sometimes worry about excessive gaming affecting studies and health.
Maintaining balance between gaming and responsibilities is very important.
Gaming communities allow players to discuss strategies and experiences.
Technology improvements continue to make games more realistic and immersive.
Virtual reality gaming provides entirely new interactive experiences.
Professional gamers practice daily to compete at high levels.
Gaming can also improve hand-eye coordination and reaction speed.
Independent developers create creative games with unique ideas and styles.
Mobile gaming has increased accessibility for casual players worldwide.
Many games encourage teamwork and communication among players.
The gaming industry creates career opportunities in design and programming.
Video games continue evolving as technology advances every year."""
]

# session state
if "paragraph" not in st.session_state:
    st.session_state.paragraph = ""

if "start_time" not in st.session_state:
    st.session_state.start_time = 0

if "mode" not in st.session_state:
    st.session_state.mode = ""

# ---------------- EASY BUTTON ---------------- #

if st.button("Easy Paragraph", key="easy_button"):

    st.session_state.mode = "easy"

    st.session_state.paragraph = random.choice(easy_paragraphs)

    st.session_state.start_time = time.time()

# ---------------- MEDIUM BUTTON ---------------- #

if st.button("Medium Paragraph", key="medium_button"):

    st.session_state.mode = "medium"

    st.session_state.paragraph = random.choice(medium_paragraphs)

    st.session_state.start_time = time.time()

# ---------------- HARD BUTTON ---------------- #

if st.button("Hard Paragraph", key="hard_button"):

    st.session_state.mode = "hard"

    st.session_state.paragraph = random.choice(hard_paragraphs)

    st.session_state.start_time = time.time()

# ---------------- SHOW PARAGRAPH ---------------- #

if st.session_state.paragraph != "":

    st.write("Type the following paragraph as fast as you can:")

    st.info(st.session_state.paragraph)

    typed_text = st.text_area(
        "Start typing here...",
        key=st.session_state.mode
    )

    if st.button("Submit"):

        end_time = time.time()

        time_taken = end_time - st.session_state.start_time

        word_count_original = len(
            st.session_state.paragraph.split()
        )

        word_count_typed = len(
            typed_text.split()
        )

        diff_words = abs(
            word_count_original - word_count_typed
        )

        wpm = (word_count_typed / time_taken) * 60

        correct_chars = 0

        paragraph = st.session_state.paragraph

        for i in range(min(len(paragraph), len(typed_text))):

            if paragraph[i] == typed_text[i]:

                correct_chars += 1

        accuracy = (
            correct_chars / len(paragraph)
        ) * 100

        st.success(f"Time Taken: {time_taken:.2f} seconds")

        st.success(f"Word Count: {word_count_typed}")

        st.success(f"Difference in Word Count: {diff_words}")

        st.success(f"WPM: {wpm:.2f}")

        st.success(f"Accuracy: {accuracy:.2f}%")