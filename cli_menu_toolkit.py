import streamlit as st
import subprocess

st.set_page_config(
    page_title="Linux Menu Based Panel", 
    page_icon="🐧",
    layout="wide",
    initial_sidebar_state="expanded"
)



st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
     
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .feature-card {
        # background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        background: #202635;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    .success-box {
        # background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
        background: #202635;
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    
    .error-box {
        # background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        background: #202635;
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    
    .info-box {
        # background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        background: #202635;
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .stSelectbox > div > div {
        border-radius: 10px;
    }
    
    .stTextInput > div > div > input {
        border-radius: 10px;
    }
    
    .metric-card {
        background: #20263;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem 0;
    }
    
    .platform-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def run_remote_command(username, ip, command):
    ssh = f"ssh {username}@{ip}"
    try:
        result = subprocess.run(f'{ssh} "{command}"', shell=True, capture_output=True, text=True, timeout=15)
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return "⏱️ SSH connection timed out."
    except Exception as e:
        return f"Error: {e}"


linux_commands = {
    "Show date": "date",
    "Show calendar": "cal",
    "List files": "ls -al",
    "Show current directory": "pwd",
    "Disk usage": "df -h",
    "Memory usage": "free -m",
    "CPU Info": "lscpu",
    "OS Info": "uname -a",
    "Top 10 processes": "top -b -n1 | head -20",
    "Current user": "whoami",
    "Show logged in users": "who",
    "System uptime": "uptime",
    "IP addresses": "ip a",
    "Network routes": "ip r",
    "Ping google": "ping -c 4 google.com",
    "List environment variables": "printenv",
    "Find file named 'test.txt'": "find / -name test.txt",
    "Search 'root' in /etc/passwd": "grep 'root' /etc/passwd",
    "Create file.txt": "touch file.txt",
    "Create directory 'testdir'": "mkdir testdir",
    "Remove file.txt": "rm file.txt",
    "Remove directory 'testdir'": "rmdir testdir",
    "Copy file.txt to copy.txt": "cp file.txt copy.txt",
    "Rename file.txt to renamed.txt": "mv file.txt renamed.txt",
    "Show file content (/etc/os-release)": "cat /etc/os-release",
    "Append 'Hello' to file.txt": "echo 'Hello' >> file.txt",
    "Change file permissions": "chmod 755 file.txt",
    "Change file owner to root": "chown root:root file.txt",
    "Show running services": "systemctl list-units --type=service",
    "Install 'tree' (apt)": "sudo apt install tree",
    "Update packages": "sudo apt update",
    "Upgrade system": "sudo apt upgrade -y",
    "Remove 'tree' (apt)": "sudo apt remove tree",
    "Check UFW firewall status": "sudo ufw status",
    "Enable UFW firewall": "sudo ufw enable",
    "Disable UFW firewall": "sudo ufw disable",
    "Show hostname": "hostname",
    "Check if port 22 is open": "ss -tuln | grep :22",
    "Reboot system": "sudo reboot",
    "Shutdown system": "sudo shutdown now",
    "List all users": "cut -d: -f1 /etc/passwd",
    "List cron jobs": "crontab -l",
    "Check open ports (netstat)": "netstat -tuln",
    "Download file with wget": "wget http://example.com",
    "Check SELinux status": "sestatus",
    "Show kernel logs": "dmesg | tail -20",
    "Show mounted filesystems": "mount | column -t",
    "Display system journal": "journalctl -xe",
    "Show current processes": "ps aux",
    "Kill process by PID": "kill -9 <PID>",
    "Check disk space of /": "du -sh /",
    "View network interfaces": "ifconfig",
    "Traceroute to google": "traceroute google.com",
    "List installed packages (Debian)": "dpkg -l",
    "Check system load": "uptime"
}


docker_commands = {
    "Launch new Ubuntu container": "docker run -dit --name mycontainer ubuntu",
    "Start container": "docker start mycontainer",
    "Stop container": "docker stop mycontainer",
    "Restart container": "docker restart mycontainer",
    "Remove container": "docker rm mycontainer",
    "List containers": "docker ps -a",
    "List running containers": "docker ps",
    "List Docker images": "docker images",
    "Pull Ubuntu image": "docker pull ubuntu",
    "Remove image": "docker rmi ubuntu",
    "Show Docker version": "docker version",
    "Show Docker info": "docker info",
    "Show container logs": "docker logs mycontainer",
    "Build Docker image": "docker build -t myimage .",
    "Save Docker image to file": "docker save -o image.tar myimage",
    "Load Docker image from file": "docker load -i image.tar",
    "Tag Docker image": "docker tag myimage newname",
    "Push image to DockerHub": "docker push myimage",
    "Prune unused images": "docker image prune -f",
    "Run Apache Webserver (port 8080)": "docker run -dit --name webserver -p 8080:80 httpd",
    "Run Nginx server (port 8081)": "docker run -dit --name nginx -p 8081:80 nginx",
    "View Docker network": "docker network ls",
    "Inspect container": "docker inspect mycontainer",
    "Check container stats": "docker stats",
    "Run interactive bash in container": "docker exec -it mycontainer bash",
    "View container file system": "docker exec -it mycontainer ls /",
    "Create Docker volume": "docker volume create myvol",
    "List Docker volumes": "docker volume ls",
    "Run with mounted volume": "docker run -dit -v myvol:/data ubuntu",
    "Create Docker network": "docker network create mynet",
    "Run container with custom network": "docker run -dit --network=mynet --name custom ubuntu",
    "List Docker contexts": "docker context ls",
    "Switch Docker context": "docker context use default",
    "Export container": "docker export mycontainer > mycontainer.tar",
    "Import container": "docker import mycontainer.tar",
    "List Docker events": "docker events",
    "Docker login": "docker login",
    "Docker logout": "docker logout",
    "Show Docker help": "docker --help",
    "Docker compose version": "docker-compose version",
    "List Docker compose services": "docker-compose ps",
    "Start Docker compose services": "docker-compose up -d",
    "Stop Docker compose services": "docker-compose down",
    "Build Linear Regression Docker Image": "docker build -t linear-regression-demo .",
    "Run Linear Regression Model": "docker run --rm linear-regression-demo"
}


st.markdown('<div class="main-header"><h1>🐧Cli-menu-toolkit</h1><p>Your Remote Linux & Docker Management Hub</p></div>', unsafe_allow_html=True)


with st.sidebar:
    st.markdown("###  Welcome to Linux Panel")
    st.markdown("---")
    
    menu = st.selectbox("Choose a Section", [
        "🏠 Dashboard", "🐧 Linux Commands", "🐳 Docker Commands"
    ])

if menu == "🏠 Dashboard":
    st.markdown('<div class="feature-card"><h2>🚀 Welcome to Your Linux Management Dashboard</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="metric-card"><h3>🐧 Linux Commands</h3><p>Remote Linux System Management</p><ul><li>System Information</li><li>File Operations</li><li>Network Commands</li><li>Process Management</li></ul></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card"><h3>🐳 Docker Commands</h3><p>Container Management</p><ul><li>Container Operations</li><li>Image Management</li><li>Network & Volumes</li><li>Machine Learning</li></ul></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box"><h3>💡 Quick Start</h3><p>Select a section from the sidebar to start managing your remote Linux systems and Docker containers!</p></div>', unsafe_allow_html=True)

elif menu == "🐧 Linux Commands":
    st.markdown('<div class="feature-card"><h2>🐧 Remote Linux Command Execution</h2></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        selected = st.selectbox("Select Command", list(linux_commands.keys()))
        user = st.text_input("SSH Username", placeholder="Enter username")
    
    with col2:
        ip = st.text_input("Remote IP", placeholder="Enter IP address")
        if st.button("🚀 Run Command", use_container_width=True):
            with st.spinner("Executing command..."):
                result = run_remote_command(user, ip, linux_commands[selected])
                st.markdown('<div class="feature-card"><h4>Command Output:</h4></div>', unsafe_allow_html=True)
                st.code(result, language="bash")

elif menu == "🐳 Docker Commands":
    st.markdown('<div class="feature-card"><h2>🐳 Docker Container Management</h2></div>', unsafe_allow_html=True)
    
    menu2 = st.sidebar.selectbox("Docker Options", [
        "🐳 Basic Commands", "🚀 RUN DIND", "🤖 Linear Regression in Docker"
    ])
    
    col1, col2 = st.columns(2)
    
    with col1:
        selected = st.selectbox("Select Docker Command", list(docker_commands.keys()))
        user = st.text_input("SSH Username", placeholder="Enter username")
    
    with col2:
        ip = st.text_input("Remote IP", placeholder="Enter IP address")
        if st.button("🐳 Run Docker Command", use_container_width=True):
            with st.spinner("Executing Docker command..."):
                result = run_remote_command(user, ip, docker_commands[selected])
                st.markdown('<div class="feature-card"><h4>Docker Output:</h4></div>', unsafe_allow_html=True)
                st.code(result, language="bash")

    if menu2 == "🚀 RUN DIND":
        st.markdown('<div class="info-box"><h3>🐳 Docker-in-Docker (DIND)</h3><p>To use Docker-in-Docker, make sure your remote VM supports it and Docker is installed inside the container.</p></div>', unsafe_allow_html=True)

    if menu2 == "🤖 Linear Regression in Docker":
        st.markdown('<div class="feature-card"><h3>🤖 Machine Learning in Docker</h3></div>', unsafe_allow_html=True)
        st.markdown("""
        **📋 Manual Steps:**
        1. Upload `Dockerfile` and `linear_regression.py` to your remote VM
        2. Use the commands above to build and run the model inside Docker
        3. Example upload command:
        ```bash
        scp Dockerfile linear_regression.py <username>@<remote_ip>:~/
        ```
        4. Then use the 'Build Linear Regression Docker Image' and 'Run Linear Regression Model' commands
        """)
