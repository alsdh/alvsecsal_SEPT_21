from silence.decorators import endpoint

@endpoint(
    route="/revisions",
    method="GET",
    sql="SELECT * FROM Revisions",
)
def get_all():
    pass



@endpoint(
    route="/revisions/$revisionid",
    method="GET",
    sql="SELECT * FROM Revisions WHERE revisionid = $revisionid",
)
def get_by_id():
    pass


@endpoint(
    route="/revisions",
    method="POST",
    sql="INSERT INTO revisions \
         (note,gradeId, professorId, date, diference) \
         VALUES \
         ($note,$gradeId, $professorId, $date, $diference)"
)
def add(note,gradeId,professorId,date,diference):
    pass



@endpoint(
    route="/revisions/$revisionid",
    method="PUT",
    sql="UPDATE revisions SET note = $note, gradeId=$gradeId, professorId = $professorId, \
         date = $date, diference = $diference\
         WHERE revisionid = $revisionid"
)
def update(note,gradeId,professorId,date,diference):
    pass



@endpoint(
    route="/revisions/$revisionid",
    method="DELETE",
    sql="DELETE FROM Revisions WHERE revisionid = $revisionid"
)
def delete():
    pass
