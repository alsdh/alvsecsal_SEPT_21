from silence.decorators import endpoint


@endpoint(
    route="/Commissions",
    method="GET",
    sql="SELECT * FROM Commissions",
)
def get_all():
    pass


@endpoint(
    route="/Commissions/$commissionid",
    method="GET",
    sql="SELECT * FROM Commissions WHERE commissionid = $commissionid",
)
def get_by_id():
    pass


@endpoint(
    route="/Commissions",
    method="POST",
    sql="INSERT INTO Commissions \
         (commissionN, professorId, people,date) \
         VALUES \
         ($commissionN, $professorId, $people, $date)"
)
def add(commissionN, professorId, people, date):
    pass


@endpoint(
    route="/Commissions/$commissionid",
    method="PUT",
    sql="UPDATE Commissions SET commissionN = $commissionN, professorId = $professorId, \
         people = $people, date = $date \
         WHERE commissionid = $commissionid"
)
def update(commissionN, professorId, people, date):
    pass


@endpoint(
    route="/Commissions/$commissionid",
    method="DELETE",
    sql="DELETE FROM Commissions WHERE commissionid = $commissionid"
)
def delete():
    pass
