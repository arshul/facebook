import facebook
import json
token  ="EAACEdEose0cBAC6kj1iEAZBah82lJwPnTUD4RkohRQoxNEMWZB0thB1SFTtaZB0Y64NsZB9ZAamlEUIa82RmulFmjzx4Wt4YtQwMfOPLtDAr3gw5S7bapB0YkQtzuigCzg1sBIXmTkDIqnet3fezCfDCvo8W0qQPsURhXsfDS56o5GDW4bBBVG5esL8XGpt7L88JmL0NZCXAZDZD"
def search(keyword):
    graph = facebook.GraphAPI(token)
    groups = graph.request('/search?q={0}&type=group'.format(keyword))
    return groups