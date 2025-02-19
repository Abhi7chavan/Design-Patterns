#Singleton design pattern ensure that class should have only one instace and which use globally all over the code.

#use case -
# i) this pattern commonly used in logging,caching,database connections,thread pools

#key points - 
# single instance - Ensure that class have only one instance.
# Global acccess - the instance is gloablly accessible 
# Lazy instantiation - the instance is created when needed
# prevent unnecessary allowcation

class logger:
    _instance = False
    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = super(logger,cls).__new__(cls)
            
        return cls._instance
    
    
    
instance_first = logger()
instance_second = logger()

print(instance_first==instance_second)
            
        
