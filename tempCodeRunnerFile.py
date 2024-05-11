from PyQt6 import QtCore, QtGui, QtWidgets
#########################################
from PyQt6.QtWidgets import QMainWindow
from os.path import join
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
import random
from PyQt6.QtWidgets import QMainWindow
import os
from PyQt6.QtSql import QSqlQueryModel
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtPrintSupport import *

from PyQt6 import QtPrintSupport, QtCore
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices,QTextImageFormat
from io import BytesIO

from barcode import Code128
from barcode.writer import ImageWriter
from PyQt6 import QtCore, QtGui, QtWidgets
import qrcode
import sqlite3
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
