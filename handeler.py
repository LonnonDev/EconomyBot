# handeler
class personhandeler(person):
	def __init__(self, person):
		self = self
		self.person = person
	def checkdb(self, person):
		c.execute("SELECT * from people WHERE name=?", (person,))
		conn.commit()
		if c.fetchone() == None:
			c.execute("INSERT INTO people (name, coins) VALUES (?, 0)", (person,))
			conn.commit()
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		if c.fetchone() == None:
			c.execute("INSERT INTO items (name, fish, fishing, fishingrods) VALUES (?, 0, 0, 0)", (person,))
			conn.commit()
		c.execute("SELECT * from inventory WHERE name=?", (person,))
		conn.commit()
		if c.fetchone() == None:
			c.execute("INSERT INTO people (name, hairdryer) VALUES (?, 0)", (person,))
			conn.commit()
		c.execute("SELECT * from levels WHERE name=?", (person,))
		conn.commit()
		if c.fetchone() == None:
			c.execute("INSERT INTO people (name, level, exp) VALUES (?, 0, 0.0)", (person,))
			conn.commit()
