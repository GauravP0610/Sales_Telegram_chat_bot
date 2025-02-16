
3️⃣ Make It Executable
Run:

bash
Copy
Edit
chmod +x ~/telegram-chatbot/start_chatbot.sh
4️⃣ Run the Script
Start both scripts in tmux by running:

bash
Copy
Edit
./start_chatbot.sh



🛠 Managing the Running Scripts
Action	Command
Detach from tmux (keep running in background)	Ctrl + b, then d
Reattach to tmux session	tmux attach -t chatrepo_session
Kill the session (stop both scripts)	tmux kill-session -t chatrepo_session
