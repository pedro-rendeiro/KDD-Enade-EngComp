import os

SENIOR_STUDENT_CODE = 0
DIR_PATH = os.path.join(os.path.dirname(__file__), "../")
NUM_ENADE_EXAM_QUESTIONS = 40
MAX_SUBJECTS_PER_QUESTION = 3
CODE_BLANK_DIS_ANSWER = 333
CODE_BLANK_OBJ_ANSWER = "."
CODE_DELETION_OBJ_ANSWER = "*"  # rasura
CODE_CANCELLED_DIS_QUESTION = 335
CODE_CANCELLED_OBJ_QUESTION = ["8", "9"]
BLANK_LABEL = "BRANCO"
CANCELLED_LABEL = "NULA"
DELETION_LABEL = "RASURA"
CODE_COURSE = 12025 #13881
STUDENT_CODE_PRESENT = 555
STUDENT_CODE_ABSENT = 222
PRESENCE_COLUMN = "TP_PRES"
DATA_DIR = "data"
ENADE_DATA_DIR = os.path.join(DATA_DIR, "enade")
SUBJECT_DF_NAME = "classificacao_charao.csv"
SUBJECT_DF_PATH = os.path.join(DATA_DIR, SUBJECT_DF_NAME)
SUBJECT_CONTENT_COLUMNS = ["conteudo1", "conteudo2", "conteudo3"]
