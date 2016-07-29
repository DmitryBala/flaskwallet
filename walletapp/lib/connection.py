from bitcoin import rpc


def get_proxy(wallet):
    # TODO flaskwallet should be able to build a service URL
    return rpc.Proxy(
        # node.rpcuser_decrypted,
        # node.rpcpass_decrypted,
        # service_url=wallet.rpchost,
        # service_port=wallet.rpcport,
        # use_https=wallet.rpchttps,
    )
