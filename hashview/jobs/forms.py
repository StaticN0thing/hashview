from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, FileField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, ValidationError
from hashview.models import Jobs


class JobsForm(FlaskForm):
    name = StringField('Job Name', validators=[DataRequired()])
    customer_id = StringField('Customer ID (unused)', validators=[DataRequired()])
    customer_name = StringField('Customer Name (unused)')
    submit = SubmitField('Next')

    def validate_job(self, name):
        job = Jobs.query.filter_by(name = name.data).first()
        if job:
            raise ValidationError('That job name is taken. Please choose a different one.')

class JobsNewHashFileForm(FlaskForm):
    name = StringField('Hashfile Name') # While required we may dynamically create this based on file upload
    file_type = SelectField('Hash Format', choices=[('', '--SELECT--'), 
                                                    ('hash_only', '$hash'), 
                                                    ('user_hash', '$user:$hash'), 
                                                    ('shadow', 'Linux/Unix Shadow File'),
                                                    ('pwdump', 'pwdump()'), 
                                                    ('NetNTLM', 'NetNTLMv1, NetNTLMv1+ESS or NetNTLMv2'), 
                                                    ('kerberos', 'Kerberos')], validators=[DataRequired()])
    hash_type = SelectField('Hash Type', choices=[  ('', '--SELECT--'),
                                                    ('0', '(0) MD5'),
                                                    ('300', '(300) MySQL4.1/MySQL5'),
                                                    ('500', '(500) md5crypt, MD5 (Unix), Cisco-IOS'),
                                                    ('1000', '(1000) NTLM '),
                                                    ('1800', '(1800) sha512crypt (Unix)'),
                                                    ('2100', '(2100) DCC2, MS Cache2'),
                                                    ('3200', '(3200) bcrypt $2*$, Blowfish (unix)'),
                                                    ('5500', '(5500) NetNTLMv1 / NetNTLMv1+ESS'),
                                                    ('5600', '(5600) NetNTLMv2'),
                                                    ('7500', '(7500) Kerberos 5 AS-REQ Pre-Auth etype 23'),
                                                    ('13100', '(13100) Kerberos 5 TGS-REP etype 23'),
                                                    ('18200', '(18200) Kerberos 5 AS-REP etype 23'),
                                                    ('19600', '(19600) Kerberos 5 TGS-REP etype 17 (AES128-CTS-HMAC-SHA1-96)'),
                                                    ('19700', '(19700) Kerberos 5 TGS-REP etype 18 (AES256-CTS-HMAC-SHA1-96)'),
                                                    ('19800', '(19800) Kerberos 5, etype 17, Pre-Auth'),
                                                    ('19900', '(19900) Kerberos 5, etype 18, Pre-Auth')], validators=[DataRequired()])
    hashfilehashes = TextAreaField('Hashes')
    hashfile = FileField('Upload Hashfile')
    submit = SubmitField('Next')

class JobsNotificationsForm(FlaskForm):
    job_completion = SelectField('Notify when Job completes', choices=[('none', 'No'),
                                                                        ('email', 'Send Email'),
                                                                        ('push', 'Send Push Notification')], validators=[DataRequired()])
    hash_completion = SelectField('Notify when specific hashes crack', choices=[('none', 'No'),
                                                                        ('email', 'Send Email'),
                                                                        ('push', 'Send Push Notification')], validators=[DataRequired()])
    submit = SubmitField('Next')

class JobSummaryForm(FlaskForm):
    submit = SubmitField('Complete')