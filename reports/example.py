# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas

# w, h = A4
# c = canvas.Canvas("hello-world.pdf", pagesize=A4)
# c.drawString(50, h - 50, "Concepto :")
# c.drawString(110, h - 50, "..................")
# c.showPage()
# c.save()

import itertools
from random import randint
from statistics import mean

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def grouper(iterable, n):
  args = [iter(iterable)] * n
  print(args)
  return itertools.zip_longest(*args)


def export_to_pdf(data):
  c = canvas.Canvas("grid-students.pdf", pagesize=A4)
  w, h = A4
  max_rows_per_page = 45
  # Margin.
  x_offset = 50
  y_offset = 50
  # Space between rows.
  padding = 15

  xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
  ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]

  for rows in grouper(data, max_rows_per_page):
    rows = tuple(filter(bool, rows))
    c.grid(xlist, ylist[:len(rows) + 1])
    for y, row in zip(ylist[:-1], rows):
      for x, cell in zip(xlist, row):
        c.drawString(x + 2, y - padding + 3, str(cell))
    c.showPage()

  c.save()


data = [("NAME", "GR. 1", "GR. 2", "GR. 3", "AVG", "STATUS")]

for i in range(1, 101):
  exams = [randint(0, 10) for _ in range(3)]
  avg = round(mean(exams), 2)
  state = "Approved" if avg >= 4 else "Disapproved"
  data.append((f"Student {i}", *exams, avg, state))

export_to_pdf(data)