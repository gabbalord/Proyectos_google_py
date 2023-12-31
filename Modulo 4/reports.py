#!/usr/bin/env python3

import os
import reportlab
from reportlab.lib.units import inch, cm
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import time
from time import strftime, gmtime
 
# using simple format of showing time

def generate(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info])



