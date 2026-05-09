# TimeTable-Notifier

## Diagram

flowchart TD
    subgraph USER["👤 User (You)"]
        UPDATE["📝 Update Excel File<br/>(When schedule changes)"]
        PHONE["📱 Phone with ntfy App<br/>(Subscribed to topic)"]
    end

    subgraph LOCAL["💻 Local PC (Initial Setup)"]
        EXCEL["📊 Timetable automate.xlsx<br/>(Schedule data)"]
        SCRIPT["🐍 send_timetable.py<br/>(Python script)"]
    end

    subgraph GITHUB["☁️ GitHub (Free Cloud)"]
        REPO["📁 Repository<br/>(TimeTable-Notifier)"]
        ACTIONS["⚙️ GitHub Actions<br/>(CI/CD Pipeline)"]
        YML["📜 send_schedule.yml<br/>(Workflow config)"]
    end

    subgraph DAILY["⏰ Daily Automation (8 PM PST)"]
        TRIGGER["🕐 Cron Trigger<br/>'0 15 * * *'"]
        RUNNER["🏃 Ubuntu Runner<br/>(GitHub Server)"]
        INSTALL["📦 Install Dependencies<br/>pandas, openpyxl, requests"]
        PARSE["📖 Parse Excel File<br/>(Find tomorrow's classes)"]
        MESSAGE["✉️ Format Message<br/>(With ✅/❌ for each slot)"]
    end

    subgraph NOTIFY["🔔 Notification Service"]
        NTFY["📡 ntfy.sh Server<br/>(Free push notifications)"]
    end

    subgraph RESULT["✅ Final Output"]
        NOTIF["🔔 Push Notification<br/>on your phone"]
    end

    %% Connections
    UPDATE -->|"git push"| REPO
    EXCEL -->|"Upload once"| REPO
    SCRIPT -->|"Upload once"| REPO
    YML -->|"Part of repo"| REPO
    
    TRIGGER --> ACTIONS
    ACTIONS --> RUNNER
    RUNNER --> INSTALL
    INSTALL --> PARSE
    REPO -.->|"GitHub downloads"| PARSE
    PARSE --> MESSAGE
    
    MESSAGE -->|"HTTP POST request"| NTFY
    NTFY -->|"Push notification"| NOTIF
    NOTIF --> PHONE

    USER -.->|"Daily at 8 PM"| NOTIF
