collection_id = 12

download_path = "downloaded"
donefile = "lists/done.txt"
failedfile = "lists/failed.txt"


class Download:
    authorization_endpoint="https://identity.insula.earth/realms/eopaas/protocol/openid-connect/auth"
    token_endpoint="https://identity.insula.earth/realms/eopaas/protocol/openid-connect/token"
    redirect_uri="http://localhost:9207/auth"
    client_id="api-client"
