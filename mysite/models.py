from django.db import models

# Create your models here.
from django.db import models


from django.contrib.auth.models import User #장고에서 기본적으로 제공하는 사용자 모델인 User 모델을 가져오는 코드
#이 코드를 사용하면 장고에서 기본적으로 제공되는 사용자 모델을 활용하여 사용자 관리를 할 수 있다
#장고 인증시스템은 사용자 관리 표준적인 모델 및 기능을 제공하며 User 모 델은 그 중 하나
#장고에서 기본적으로 제공되는 모델을 활용 User는 계정정보를 저장하고 관리, 사용자이름, 메일, 비밀번호 해시 정보를 포함
#사용자 등록, 로그인, 비밀번호 변경 등의 기능을 개발할 때 user모델을 사용하여 정보 저장 및 관리 가능
#contrib.auth 앱은 사용자 인증과 관련된 여러가지 기능을 제공하여 보안성 높은 관리를 구현할 수 있다
#장고 2.0부터는 커스텀 사용자 모델 정의를 권장한다 기존 User모델에 새로운 필드를 추가 또는 동작 수정이 가능
#user모델은 contrib.auth 앱에 포함되어 있다. 이 앱은 인증,뷰,폼,백엔드 등을 제공한다
#user모델은 인증 시스템에서 사용자 정보를 관리하는 데에 쓰인다.
#user모델은 대부분의 App에서 공통적으로 사용되는 인증 관련 모델
#만약 커스텀 사용자 모델을 정의한다면 장고 공식문서를 참조한다


class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

# 주어진 코드는 Django에서 모델을 정의하는 클래스인 MainContent를 나타냅니다.
# 모델은 데이터베이스 테이블을 생성하고 관리하는 데 사용됩니다.
# 해당 모델의 구성 요소:
# title: CharField로 정의되어 있으며, 최대 길이가 200인 문자열을 저장할 수 있는 필드입니다.
# 주로 제목이나 간단한 문자열 정보를 저장하는 데 사용됩니다.
# content: TextField로 정의되어 있으며, 긴 텍스트나 문단을 저장할 수 있는 필드입니다.
#  제한 없이 많은 텍스트를 저장할 수 있습니다.
# pub_date: DateTimeField로 정의되어 있으며, 날짜와 시간을 저장하는 필드입니다.
# 'date published'는 필드의 레이블(label)로 사용되며, 이 필드는 해당 데이터가 언제 작성되었는지를 나타냅니다.
# str 메소드: 객체를 문자열로 표현하기 위해 사용되는 특수 메소드입니다.
# 이 메소드는 주로 개발자가 객체를 쉽게 확인하고 디버깅할 수 있도록 도와줍니다.
# 여기서는 title을 반환하여 객체가 문자열로 표현될 때 제목이 사용되도록 설정되어 있습니다.
# 이러한 Django 모델은 데이터베이스에 MainContent 테이블을 생성하고,
# 해당 테이블의 각 레코드는 제목, 내용, 발행 날짜의 정보를 저장할 수 있습니다.




#Comment 클래스를 생성한다. 새로운 데이터 모델을 정의한다. 장고의 models 클래스를 상속 받아서 장고 모델로 정의함
#따라서 장고의 모델은 데이터베이스와 연관된 구조를 파이썬 클래스로 표현한 것이다
#일반적으로 클래스는 객체지향프로그래밍에서 사용되는 개념으로 데이터와 메서드(함수)를 포함하는 것을 말한다
#장고에서 모델은 클래스의 한 종류로 데이터베이스와 상호 작용을 위해 특별히 디자인 된 클래스이다
#따라서 장고에서 모델은 파이썬클래스이며 이것은 데이터베이스 테이블의 구조를 정의하는 역할을 말한다
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #외래 키 관계, 각 코멘트는 특정 사용자와 연결, on_delete 옵션은 사용자가 삭제 될 때 해당 사용자와 연결 된 코멘트도 함께 삭제 된다
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE) #모델과 외래키 관계, 코멘트는 특정 MainContent와 연결, on_delete 옵션은 해당 메인콘텐츠가 삭제 될 때 연결 된 코멘트도 함께 삭제
    content = models.TextField() #코멘트의 내용을 나타내는 TextField 사용자가 작성한 코멘트의 내용이 여기에 저장
    create_date = models.DateTimeField(auto_now_add=True) #코멘트가 생성 된 날짜와 시간을 나타내는 DateTimeField, auto_now_add 옵션은 모델이 저장되는 순간의 날짜와 시간이 자동으로 갱신
    modify_date = models.DateTimeField(auto_now=True) #코멘트가 수정 된 날짜와 시간을 나타내는 DateTimeField, auto_now 옵션은 모델이 저장될 때마다 수정된 날짜와 시간 갱신

