from mtexam_get_database import get_database

mydb = get_database()
collection_name = mydb["blood"]

n = mydb.list_collection_names()
print(n)

Q000001 = {
    "_id": "Q000001",
    "question": "若病人 Hb 為 10.5 g/dL，MCV 為 110 fL，MCHC 為 34%，則此病人最可能為下列何種類型的貧血?",
    "A": "Normocytic，Normochromic",
    "B": "Macrocytic，Hyperchromic",
    "C": "Macrocytic，Normochromic",
    "D": "Normocytic，Hyperchromic",
    "answer": "C",
    "year": "112-1",
}

Q000002 = {
    "_id": "Q000002",
    "question": "在細胞中，vitamin B<sub>12</sub> 在 methyltetrahydrofolate 轉換成 tetrahydrofolate 的反應扮演重要角色。在此反應中，homocysteine 會轉變成下列那一個胺基酸?",
    "A": "Methionine",
    "B": "Cysteine",
    "C": "Tryptophan",
    "D": "Glycine",
    "answer": "A",
    "year": "112-1",
}

collection_name.insert_many([Q000001, Q000002])
