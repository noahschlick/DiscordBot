from dotenv import load_dotenv
import bot 

if __name__ == "__main__":
    print("***********************Attempting to RUNNN ***************************")
    load_dotenv()
    print("***********************Loaded dotenv ***************************")
    bot.run_discord_bot()