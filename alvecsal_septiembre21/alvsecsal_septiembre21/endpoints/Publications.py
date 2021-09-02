from silence.decorators import endpoint

@endpoint(
    route="/publications",
    method="GET",
    sql="SELECT * FROM Publications",
)
def get_all():
    pass

@endpoint(
    route="/publications/$publicationid",
    method="GET",
    sql="SELECT * FROM Publications WHERE publicationid = $publicationid",
)
def get_by_id():
    pass


@endpoint(
    route="/publications",
    method="POST",
    sql="INSERT INTO Publications \
        (publicationid,name,professorId,total,date,paper) \
        VALUES \
        ($publicationid,$name,$professorId,$total,$date,$paper)"
)
def add(publicationid,name,professorId,total,date,paper):
    pass



@endpoint(
    route="/publications/$publicationid",
    method="DELETE",
    sql="DELETE FROM publications WHERE publicationid = $publicationid",
)
def delete():
    pass



@endpoint(
    route="/publications/$publicationid",
    method="PUT",
    sql="UPDATE Publications" 
        +" SET"
        + " publicationid = $publicationid, name = $name, professorId=$professorId, total=$total, date=$date, paper=$paper" 
        + " WHERE publicationid = $publicationid" 
)
def update(publicationid,name,professorId,total,date,paper):
    pass

