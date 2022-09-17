class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.token = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token.keys() and self.token[tokenId] > currentTime:
            self.token[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(currentTime < v for _, v in self.token.items())
