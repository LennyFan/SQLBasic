### Basic Structure

```sql
SELECT # select the attributes
FROM # from relations/tables
JOIN ON # combine two table
WHERE # add th condition
GROUP
ORDER
LIMIT # data length
```


SELECT

```sql
# remove duplicate
SELECT distinct *
# keep duplicate
SELECT all *
```
- the attributes under SELECT suport the operators +,-,* and /
```sql
SELECT GPA*999 from Students;
```

WHERE
```sql
# and
where attribute1 = "Lenny" and attribute2 =  "Test"
# or
where attribute1 = "Lenny" or attribute2 =  "Test"
# have a but not b
where attribute1 = "Lenny" not attribute2 =  "Test"
# between 
# 0 <= a <= 99
where score between 0 and 99
```

FROM

```sql
# product axb
SELECT * from a, b
> return all combination of a and b
# join
SELECT * 
from a,b 
where a.attribute_in_A = b.attribute_in_B
```

as
```Mysql
# replace column name
SELECT A as a
from B as b, C as c
where c.attribute = b.attribute
```

Order by


String Opeartions
- percent (%) have sub string 
- underscore (_)



Having


***

**Update entry value**
```sql
Update table
set a = '' where condition;

update table
set a = CASE
    when (a in "" / a = "") then ___
    when (a in "" / a = "") then ___
    else ''
end
```


***
 
## SparkSQL

```python
## create spark dataframe
sqdf = spark.createDataFrame(....)

## read 
# spark.read.datatype()
df = spark.read.csv() 
df = spark.read.json()

df.show()

## basic structure
# in dataframe
df.select('colum').show()

# in sql lenguage
df.createOrReplaceTempView("df")
sqlDF = spark.sql("SELECT column FROM df")
sqlDF.show()
 
## write
df.write.datatype()
```
