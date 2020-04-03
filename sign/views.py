import tensorflow as tf
import numpy as np
from tensorflow import keras
from django.shortcuts import render
from .models import user


def add(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('age'):
            post = user()
            post.name = request.POST.get('name')
            post.age = request.POST.get('age')
            post.save()
            t = user.objects.all()
            return render(request, 'main.html', {'t': t})

    else:
        return render(request, 'base.html')


def added(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('age'):
            post = user()
            post.name = request.POST.get('name')
            post.age = request.POST.get('age')
            post.save()
    re = user.objects.all()
    for x in re:
        p = int(x.age)

    model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

    model.compile(optimizer='sgd', loss='mean_squared_error')

    xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
                   1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], dtype=float)
    ys = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
                   1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], dtype=float)

    model.fit(xs, ys, epochs=50)

    t = model.predict([p])

    return render(request, 'main.html', {'t': t})
