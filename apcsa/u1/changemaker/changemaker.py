import check50

@check50.check()
def exists():
  """File (ChangeMaker.java) Exists"""
  check50.exists("ChangeMaker.java")

@check50.check()
def compiles(exists):
  """File (ChangeMaker.java) Compiles"""
  check50.run("javac ChangeMaker.java").exits("ChangeMaker.class")

@check50.check()
def test0(compiles):
  """Test0"""
  check50.run("java ChangeMaker").stdin("0.00\n0.00").stdout("Hello, world!", regex=False).exit(0)
