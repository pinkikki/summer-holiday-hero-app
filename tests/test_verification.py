from app import verification


def test_verify_scene_name():
    assert verification.verify_scene_name('classroom')
