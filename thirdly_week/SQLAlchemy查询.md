# SQLAlchemy查询

## 基本查询语句
```python
session.query(User).all()	# 查询User类的全部实例

session.query(User).first()  	# 查询第一条数据

session.query(User).filter(User.name=='王麻子').all()	# 在User类中所有叫王麻子的实例

session.query(User).filter(User.id>=6).all() 	# 查询id大于6的全部实例

session.query(User.name).all()		# 查询User表中全部数据的name值

session.query(User).filter(User.email.like('%gmeail%')).all() 	# 查询User中邮箱为gmail的实例

#多段条件查询
from sqlalchemy import in_, and_, or_

session.query(User).filter(User.name.in_(['张三', '李四', '王麻子'])).all()	# 查询张三，李四，王麻子在实例中吗

session.query(User).filter(and_(User.name=='张三', User.id==1)).all()	# 查询姓名为张三，id为1的实例

session.query(User).filter(or_(User.name=='张三', User.id==3)).all() 	# 要么name为张三，要么id为3的实例

```

## 高级查询语句
1. 下面介绍 SQLAlchemy 的排序、设置查询数量、联结查询等操作。

### 排序

```python
session.query(User).order_by(User.email).all()	# 以email的值排序，默认升序

session.query(User).order_by(User.email.desc()).all()	# 降序

```

### 查询数量

```python
session.query(User).order_by(User.id.desc()).limit(4).all()	# 降序排序，取前4个

session.query(User).filter(User.email.like('%gmail%')).count()	# 查询邮箱为gmail的实例个数
```

### 联结查询

```python
session.query(Course).join(User).filter(User.name=='王雷').all()	# 查询王雷老师的全部课程，即查询course表中的数据，条件为name的值为'王雷'的user表外键关联的course表中的数据。
```
