########################################################################
#
#   1. Adding steps to install VMware tools for desktop
#   2. Install ssh
#   3. Git install
#   4 ifconfig
#
########################################################################


1. Adding steps to install VMware tools for desktop.
    
    Step 1: sudo apt-get install opven-vm-tools-desktop

2. Install ssh
    
    Step 1: sudo apt update
    Step 2: sudo apt install openssh-server
    Step 3: Check command --> sudo systemctl status ssh
    Step 4 ifconfig


3. Git Intall.
    Step 1: sudo apt-get install git-all
    Step 2: git --version

4. ifconfig
    m@m:~$ ifconfig
    Command 'ifconfig' not found, but can be installed with:
    Step 1: sudo apt install net-tools

5. SSH keygen setup
    Tut : https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-1604

    m@m:~$ ssh-keygen -b 4096
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/m/.ssh/id_rsa): 
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Saving key "/home/m/.ssh/id_rsa" failed: passphrase is too short (minimum five characters)
    m@m:~$ ssh-keygen -b 4096
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/m/.ssh/id_rsa): 
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /home/m/.ssh/id_rsa.
    Your public key has been saved in /home/m/.ssh/id_rsa.pub.
    The key fingerprint is:
    SHA256:riM8A1f7UcBx1WuyJdtw7onN5HPw3fMBagCewMH2jrk m@m
    The key's randomart image is:'
    +---[RSA 4096]----+
    |    .. .......   |
    |    .o. o.    .  |
    |    .o.. .     . |
    |      +.o . + =  |
    |     .++So   &   |
    |  . .o.o. . + *  |
    |   +  .... o B =o|
    |    =E... . . B.*|
    |     +..       o+|
    +----[SHA256]-----+
    m@m:~$ cat ~/.ssh/id_rsa.pub
    ssh-rsa key
    m@m:~$ 
    m@m:~$ 
    ############################################################################
    ############################################################################

    m@m:~/Python_practice$
    m@m:~/Python_practice$ git clone git@github.com:Aditsh82/Python_practice.git
    Cloning into 'Python_practice'...
    The authenticity of host 'github.com (13.234.176.102)' can't be established.'
    RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added 'github.com,13.234.176.102' (RSA) to the list of known hosts.
    Enter passphrase for key '/home/m/.ssh/id_rsa':
    remote: Enumerating objects: 3, done.
    remote: Counting objects: 100% (3/3), done.
    remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
    Receiving objects: 100% (3/3), done.
    m@m:~/Python_practice$
    m@m:~/Python_practice$
    m@m:~/Python_practice$ ls
    Python_practice

6. git stuff

    1. switching beanches
        m@m:~/Python_practice/Python_practice$
        m@m:~/Python_practice/Python_practice$ git checkout master
        Switched to branch 'master'
        Your branch is up to date with 'origin/master'.

    https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-locally-and-remotely

        m@m:~/Python_practice/Python_practice$ git branch -D test_beanch_1
        Deleted branch test_beanch_1 (was 0fda861).
        m@m:~/Python_practice/Python_practice$

7. some usefull commands:
    for disk space --> du -sh