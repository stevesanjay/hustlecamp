# Authorization Decorator to Check User Permissions:

def requires_permission(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if check_permission(permission):
                return func(*args, **kwargs)
            else:
                raise PermissionError("You don't have permission to access this resource")
        return wrapper
    return decorator

def check_permission(permission):
    # Function to check user permissions (mocked)
    user_permissions = ['read', 'write']
    return permission in user_permissions

@requires_permission('write')
def edit_document(document):
    print(f"Editing document: {document}")

edit_document("example.txt")