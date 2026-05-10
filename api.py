from typing import List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, ModelSchema

from .models import Car


api = NinjaAPI()


class CarOut(ModelSchema):
    class Config:
        model = Car
        model_fields = ["id", "brand", "model", "year", "price"]


class CarIn(ModelSchema):
    class Config:
        model = Car
        model_fields = ["brand", "model", "year", "price"]


@api.get("/car", response=List[CarOut])
def list_cars(request):
    return Car.objects.all()


@api.get("/car/{car_id}", response=CarOut)
def get_car(request, car_id: int):
    return get_object_or_404(Car, id=car_id)


@api.post("/car", response=CarOut)
def create_car(request, data: CarIn):
    car = Car.objects.create(**data.dict())
    return car


@api.put("/car/{car_id}", response=CarOut)
def update_car(request, car_id: int, data: CarIn):
    car = get_object_or_404(Car, id=car_id)

    for attr, value in data.dict().items():
        setattr(car, attr, value)

    car.save()
    return car


@api.delete("/car/{car_id}")
def delete_car(request, car_id: int):
    car = get_object_or_404(Car, id=car_id)
    car.delete()

    return {"success": True}
    
