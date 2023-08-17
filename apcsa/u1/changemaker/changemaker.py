import check50

@check50.check()
def exists():
  """File (ChangeMaker.java) Exists"""
  check50.exists("ChangeMaker.java")

@check50.check()
def compiles(exists):
  """File (ChangeMaker.java) Compiles"""
  check50.run("javac ChangeMaker.java")
  check50.exists("ChangeMaker.class")

@check50.check()
def test0(compiles):
  """Test $0.00"""
  expected = ["$ 20.00: 0",
              "$ 10.00: 0",
              "$  5.00: 0",
              "$  1.00: 0",
              "$  0.25: 0",
              "$  0.10: 0",
              "$  0.05: 0",
              "$  0.01: 0" ]
  result = check50.run("java ChangeMaker").stdin("0.00\n0.00").stdout()
  for e in expected:
    help = None
    if e not in result:
        help = "Incorrect change given:\Expected: " + e
        raise check50.Failure(help)

@check50.check()
def test3641(test0):
  """Test $36.41"""
  expected = ["$ 20.00: 1",
              "$ 10.00: 1",
              "$  5.00: 1",
              "$  1.00: 1",
              "$  0.25: 1",
              "$  0.10: 1",
              "$  0.05: 1",
              "$  0.01: 1" ]
  result = check50.run("java ChangeMaker").stdin("63.59\n100.00").stdout()
  for e in expected:
    help = None
    if e not in result:
        help = "Incorrect change given:\Expected: " + e
        raise check50.Failure(help)
