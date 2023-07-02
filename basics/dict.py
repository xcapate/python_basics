def deref_multi(data, keys):
    return deref_multi(data[keys[0]], keys[1:]) \
        if keys else data



data={
    "team":{
        "controller":{"fullname":"Bob Esponja"}
    }
}

fullname='team.controller.fullname'

last = deref_multi(data, fullname.split('.'))
print(last)





