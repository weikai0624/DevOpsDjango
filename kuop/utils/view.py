from functools import wraps
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

def validate_request_serializer(serializer_class_attr="serializer_class"):
    """
    用 decorator 自動做 request validation serializer_class
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            # 取 view 的 serializer_class
            serializer_class = getattr(self, serializer_class_attr, None)
            if serializer_class is None:
                raise AttributeError(f"{self.__class__.__name__} 必須設定 {serializer_class_attr}")

            serializer = serializer_class(data=request.data)

            try:
                serializer.is_valid(raise_exception=True)
            except ValidationError as e:
                return Response({"detail": e.default_detail, "validation_errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

            # 將 validated_data 傳給 view 方法
            request.validated_data = serializer.validated_data

            return func(self, request, *args, **kwargs)
        return wrapper
    return decorator
