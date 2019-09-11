import time
import os
import sys

def verluchie():
	try:
		
		os.system('echo "\\e[4;34mStarting verluchie Script----------------------->\\e[0m"')
		os.system('apt install autoconf bison clang coreutils curl findutils git apr apr-util libffi \
					libgmp libpcap postgresql readline libsqlite openssl libtool libxml2 \
					libxslt ncurses pkg-config postgresql wget make ruby libgrpc ncurses-utils termux-tools gem -y')
		os.system('echo "####################################"')
		os.system('echo "Downloading & Extracting....."')
		
		os.system("cd $HOME && curl -LO https://github.com/rapid7/metasploit-framework/archive/4.16.4.tar.gz && tar -xf $HOME/4.16.4.tar.gz && \
					mv $HOME/metasploit-framework-4.16.4 $HOME/metasploit-framework && cd $HOME/metasploit-framework && sed '/rbnacl/d' -i Gemfile.lock && \
					sed '/rbnacl/d' -i metasploit-framework.gemspec && gem install bundler && bundle config build.nokogiri --use-system-libraries && \
					gem install nokogiri -- --use-system-libraries && sed 's|grpc (.*|grpc (1.4.1)|g' -i $HOME/metasploit-framework/Gemfile.lock  && gem unpack grpc -v 1.4.1 && cd grpc-1.4.1 && \
					curl -LO https://raw.githubusercontent.com/grpc/grpc/v1.4.1/grpc.gemspec && curl -L https://wiki.termux.com/images/b/bf/Grpc_extconf.patch -o extconf.patch && \
					patch -p1 < extconf.patch && gem build grpc.gemspec && gem install grpc-1.4.1.gem && cd .. && rm -r grpc-1.4.1 && cd $HOME/metasploit-framework && bundle install -j5")
		
		os.system("$PREFIX/bin/find -type f -executable -exec termux-fix-shebang \{\} \;")
		os.system("rm ./modules/auxiliary/gather/http_pdf_authors.rb")
		os.system("ln -s $HOME/metasploit-framework/msfconsole /data/data/com.termux/files/usr/bin/")
	except KeyboardInterrupt as e:
		print("\nExiting_*_*_*_*_*_")
		sys.exit(1)
	
def Auxilus():
	try:
		os.system('echo "\\e[4;34mStarting Auxilus Script----------------------->\\e[0m"')
		os.system("pkg update && pkg upgrade -y && pkg install curl wget tsu wget git && wget Auxilus.github.io/metasploit.sh && bash metasploit.sh ")
	except KeyboardInterrupt as e:
		print("\nExiting_*_*_*_*_*_")
		sys.exit(1)
		
def R3tr0Gh0s7():
	try:
		os.system('echo "\\e[4;34mStarting R3tr0Gh0s7 Script----------------------->\\e[0m"')
		os.system("apt update && apt upgrade && apt install unstable-repo && apt install metasploit")
	except Exception as e:
		print("\nExiting_*_*_*_*_*_")
		sys.exit(1)
		
def TechX3():
	try:
		os.system('echo "\\e[4;34mStarting TechX-3 Script----------------------->\\e[0m"')
		os.system("apt update && apt upgrade && apt install curl && \
						curl -LO raw.githubusercontent.com/1Tech-X/Metasploit-4.16.12/master/metasploit.sh && \
						chmod 777 metasploit.sh && sh metasploit.sh")
	except KeyboardInterrupt as e:
		print("\nExiting_*_*_*_*_*_")
		sys.exit(1)
		
def Hax4Us():
	try:
		os.system('echo "\\e[4;34mStarting Hax4Us Script----------------------->\\e[0m"')
		os.system("pkg update && pkg upgrade && pkg install git curl wget nmap -y && \
					curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh && chmod 777 metasploit.sh && ./metasploit.sh")
	except KeyboardInterrupt as e:
		print("\nExiting_*_*_*_*_*_")
		sys.exit(1)
		
def W1nteFr3ak():
	os.system('echo "\\e[4;34mStarting W1nterFr3ak Script----------------------->\\e[0m"')
	os.system('echo "\\e[1;34mI am about to setup the Termux repo install the keys and proceed to install metasploit\\e[0m"')
	action = input("Winter TERMUX setup, alow (Y or y| N or n):")
	#sudo
	if action.lower() == 'n':
		os.system("clear")
		main()
	elif action.lower() == 'y':
		os.system('echo "\\e[4;34mConfiguring Repo----------------------->\\e[0m"')
		os.system("apt update && apt upgrade && pkg install git && git clone https://gitlab.com/st42/termux-sudo && cd termux-sudo && \
						pkg install ncurses-utils && cat sudo > /data/data/com.termux/files/usr/bin/sudo && \
						chmod 700 /data/data/com.termux/files/usr/bin/sudo && pkg install tsu")
		os.system("pkg upgrade && pkg install wget curl dirmngr gnupg-curl \
						autoconf automake bison bzip2 clang cmake coreutils diffutils flex gawk git grep \
						gzip libtool make patch perl sed silversearcher-ag tar && \
						apt-key adv --keyserver pgp.mit.edu --recv A46BE53C &&  mkdir -p $PREFIX/etc/apt/sources.list.d && \
						apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 379CE192D401AB61")
		os.system('echo "deb [trusted=yes] https://grimler.se root stable" > $PREFIX/etc/apt/sources.list.d/termux-root.list && apt update')
		verluchie()
		
def main():
	os.system('echo "\\e[1;34m Created By W1nterFr3ak\\e[0m"')
	os.system('echo "\\e[1;32m 60% credits goes to you;;; \\e[0m"')
	os.system('echo "\\e[1;32m Mail: WinterFreak@protonmaail.comm \\e[0m"')
	print('\n')
	print("Their are various  methods to install metasploit here are  some  from  popular 1337s")
	os.system('echo "\\e[1;34m 1) verluchie\\e[0m"')
	os.system('echo "\\e[1;34m 2) R3tr0Gh0s7\\e[0m"')
	os.system('echo "\\e[1;34m 3) TechX3\\e[0m"')
	os.system('echo "\\e[1;34m 4) Hax4Us\\e[0m"')
	os.system('echo "\\e[1;34m 5) W1nteFr3ak (For beginners Termux Sets Up)\\e[0m"')
	try:
		act = input("Choose your Option  :")
		if act == '1':
			verluchie()
			
		elif act == '2':
			R3tr0Gh0s7()
			
		elif act == '3':
			TechX3()
			
		elif act == '4':
			Hax4Us()
			
		elif act == '5':
			W1nteFr3ak()
			
		else:
			print("\nExiting_*_*_*_*_*_")
			sys.exit(1)
	except KeyboardInterrupt as e:
		print("\nExiting_*_*_*_*_*_")
	
	
if __name__  == "__main__":
	main ()
	
	
	
		
