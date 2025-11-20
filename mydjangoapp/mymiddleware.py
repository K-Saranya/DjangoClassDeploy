class MyMiddleware():
    def __init__(self, response):
        self.response = response
        
    def __call__(self, request):
        print("Before View...")
        result = self.response(request)
        print("After View...")
        return result
    