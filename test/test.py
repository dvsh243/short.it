
# python, html, css, javascript, mongodb, docker 

'''v1'''
# BACK-END
# POST /api/create -> create tiny url
# GET /h98g1hg0 -> redirect to url (MD5 hashing)
# GET /h98g1hg0/analytics -> redirection analytics


# fix hash collision
# rate limiting


# FRONT-END
# -> create tiny url
# -> analytics (total clicks, location wise clicks)

'''
analytics data example -> 
{
    'total' : 89115,
    'location': {
        'India' : 7148,
        'Nigeria' : 9015,
        'US': 4924
    }
}
'''


'''v2'''
# api/create -> create tiny url
# lock -> ask password before redirection
# login
# show my created tiny urls
# analytics -> url clicks and locations