from silence.decorators import endpoint
@endpoint(
    route="/awards",
    method="GET",
    sql="SELECT * FROM awards",
)
def get_all():
    pass

@endpoint(
    route="/awards/$awardid",
    method="GET",
    sql="SELECT * FROM awards WHERE awardid = $awardid",
)
def get_by_id():
    pass

@endpoint(
    route="/awards",
    method="POST",
    sql="INSERT INTO awards \
        (awardid,studentId,degreeId,award,year,note) \
        VALUES \
        ($awardid,$studentId,$degreeId,$award,$year,$note)"
)
def add(awardid,studentId,degreeId,award,year,note):
    pass

@endpoint(
    route="/awards/$awardid",
    method="DELETE",
    sql="DELETE FROM awards WHERE awardid = $awardid",
)
def delete():
    pass

@endpoint(
    route="/awards/$awardid",
    method="PUT",
    sql="UPDATE awards" 
        +" SET"
        + " awardid = $awardid, studentId = $studentId, degreeId=$degreeId, award=$award, year=$year, note=$note" 
        + " WHERE awardid = $awardid" 
)
def update(awardid,studentId,degreeId,award,year,note):
    pass