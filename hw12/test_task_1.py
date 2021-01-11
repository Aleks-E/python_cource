# from alembic.config import Config
# from alembic import command
# from sqlalchemy import create_engine, MetaData
#
#
# # from task_1 import meta
# # from task_1 import engine, meta
#
#
#
#
# engine = create_engine('sqlite:///test.db', echo=True)
# meta = MetaData()
# # meta.create_all(engine)
# cfg = Config("alembic_1.ini")
#
# with engine.begin() as connection:
#     cfg.attributes['connection'] = connection
#     # command.upgrade(cfg, "head")
#     command.downgrade(cfg, "base")

# meta.create_all(engine)



# meta.create_all(engine)

# alembic_cfg = Config("alembic.ini")
# command.stamp(alembic_cfg, "head")


# with engine.begin() as connection:
#     alembic_cfg.attributes['connection'] = connection
#     command.upgrade(alembic_cfg, "head")



    # command.downgrade(alembic_cfg, "base")