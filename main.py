from ai.engineer import RaceEngineer
from voice.tts import TTS


def main():

    engineer = RaceEngineer()
    tts = TTS()

    setup = """
rear anti roll bar: 6
rear wing: 8
rear tire pressure: 27.5
"""

    while True:

        problem = input("\nDriver: ")

        response = engineer.analyze_problem(problem, setup)

        tts.speak(response)


if __name__ == "__main__":
    main()