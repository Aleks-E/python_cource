from hw6.task_2 import instances_counter


def test_number_of_created_instanses():
    @instances_counter
    class SomeClass:
        ...

    assert SomeClass.get_created_instances() == 0
    SomeClass(), SomeClass(), SomeClass()
    assert SomeClass.get_created_instances() == 3


def test_reset_number_of_created_instanses():
    @instances_counter
    class SomeClass:
        ...

    SomeClass(), SomeClass(), SomeClass()
    assert SomeClass.get_created_instances() == 3
    assert SomeClass.reset_instances_counter() == 3
    assert SomeClass.get_created_instances() == 0
