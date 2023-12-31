# LoL-AFK-Bot
The fully automated afk bot for Co-op vs. AI gamemode. We implement this AFK bot only with Pydirectinput and OpenCV, so it might be undetectable.

This project is designed for TW server. If you want to run this code on other server, you have to replace the templates corresponding to your GUI to ensure our program can find the target from your screen.

https://github.com/cwLin1/LoL-AFK-Bot/assets/61427980/8fd34c17-85a5-4a0e-9c66-23f289cb62b4

## Requirements
```
opencv-python
pydirectinput
```

## How to run
1. Before running, you have to make sure all of your abilities are set to smart cast, hotkey and GUI settings are in default.
  
    ![image](https://github.com/cwLin1/LoL-AFK-Bot/assets/61427980/d9ad19c9-c3b6-46ac-aaf3-0c32cd21b90b)
    ![image](https://github.com/cwLin1/LoL-AFK-Bot/assets/61427980/b0fc1bd9-314d-4f5d-b144-3132bdbe6451)

2. Open your LoL client and start a party.

    ![image](https://github.com/cwLin1/LoL-AFK-Bot/assets/61427980/bf4017ea-f36d-4b94-9013-30ee55468b07)

3. Run the code with following commands. (We use Sona bot in this example.)
    ```
    cd <Project Folder>/sona_bot
    python bot.py
    ```

4. Insert the number of games that you want to AFK.

     ![image](https://github.com/cwLin1/LoL-AFK-Bot/assets/61427980/d3bcf35d-04a5-44bb-a39a-50dfb4f4d61b)

If you are already in the game, then run ```python ingame.py```, our program will finish the game autoamtically.

