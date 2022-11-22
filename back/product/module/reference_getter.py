from ..models import reference
from ..serializers.serializers import referenceSerializer
import json

def find_reference(problem_id):
    try:
        item = (reference.objects
                        .filter( problem= problem_id)
                    )
        serializer = referenceSerializer(item, many=True)
        return serializer.data
    except Exception as e:
        print(e)
        return 0
