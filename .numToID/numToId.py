o
    �X�bd  �                   @   s�   d dl Z d dlZd dlZzd dlZW n   e �d� d dlZY dZdZdZdZdZ	dZ
dZd	Zd
Ze �d� dd� Zdd� Zdd� Zz	e�  e�  W dS  eyZ   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35m�clearc                   C   s,   t �d� t �d� t �d� t �d� d S )N�..zlolcat banner.shz.Textzlolcat MyText.txt)�os�chdir�system� r   r   �
numToId.py�header   s   


r	   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr   r   r   �	logoprint&   s
   
�r   c                  C   sd  t ttd t ��} t�d�j}ddlm} d|  }|� }||d< d|d< z	tj||d	�}W n   t	d
� Y |�
� d dkrot	td � t ttd t ��}|dkrit�d� t�d� t�d� t�d� d S t��  d S zt	td t |�
� d d  � W n
   t	td � Y zt	td t d |�
� d d  � W n
   t	td � Y zt	td t |�
� d d  � W n
   t	td � Y zt	td t |�
� d d  � W n
   t	td � Y zt	td t |�
� d d   � W n
   t	td � Y zt	td! t |�
� d d"  � W n
   t	td! � Y zt	td# t |�
� d d$  � W n
   t	td% � Y zt	td& t |�
� d d'  � W n
   t	td& � Y zt	td( t |�
� d d)  � W n
   t	td* � Y zt	td+ t |�
� d d,  � W n
   t	td+ � Y zt	td- t |�
� d d.  � W n
   t	td- � Y zt	td/ t |�
� d d0  � W n
   t	td/ � Y zt	td1 t |�
� d d2  � W n
   t	td3 � Y zt	td4 t |�
� d d5  � W n
   t	td4 � Y t ttd t ��}|dk�r,t�d� t�d� t�d� t�d� d S t��  d S )6Nz

     Enter Number: z!https://pastebin.com/raw/RptmpLnKr   )�CaseInsensitiveDictzMhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=getUserInfo&msisdn=88z	x-api-keyZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key)�headersz>
     Your Request Rejected.Please Use VPN or Try Again Leter Zrdescz	Not foundz     User Not foundz"

     Press Enter For Again Find � r   z.numToIDzpython numToId.py�   z

     Nickname: �dataZnicknamez     Nickname: z     Number: �+Zmsisdnz     Name: �namez     Points: Zpointsz     Followers: Z	followersz     Following: Z	followingz     Shouts: Zupdatesz     Shouts:z     Comments: Zcommentsz     Friends: Zfriendsz     Friends:z     Gender: Zgenderz     Birthday: Zbirthdayz     Lastseen: Z	timestampz     Start Date: Z
start_datez     Start Date:z     End Date: Zend_date)�str�input�green�yellow�requests�get�textZrequests.structuresr   �printZjson�red�cyan�purpler   r   r   r   r   r   �exit)�user�keyr   Zurlr   ZrespZenterr   r   r   �main-   s�   



$($$$$$$$$$$$$



r(   )r   r   r   r   r   ZblueZ	lightbluer"   Zwhiter   r   r#   �endr$   r	   r   r(   �KeyboardInterruptr%   r   r   r   r   �<module>   s2   


^�