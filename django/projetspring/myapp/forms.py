from django.forms import Form
from django import forms



type_CHOICES = (
    ("ADMIN", "ADMIN"),
    ("USER", "USER"),

)

class signupform(Form):

    firstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))





class SymptomsForm(forms.Form):
    itching = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline col-lg-4'}), initial='no')
    skin_rash = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    nodal_skin_eruptions = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    continuous_sneezing = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    shivering = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    chills = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    joint_pain = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    stomach_pain = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    acidity = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    ulcers_on_tongue = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    muscle_wasting = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    vomiting = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    burning_micturition = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    spotting_urination = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    fatigue = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    weight_gain = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    anxiety = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    cold_hands_and_feets = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    mood_swings = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    weight_loss = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    restlessness = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    lethargy = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    patches_in_throat = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    irregular_sugar_level = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    cough = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    high_fever = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    sunken_eyes = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    breathlessness = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    sweating = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    dehydration = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    indigestion = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect(attrs={'class': 'radio-inline'}), initial='no')
    headache = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    yellowish_skin = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    dark_urine = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    nausea = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    loss_of_appetite = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    pain_behind_the_eyes = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    back_pain = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    constipation = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    abdominal_pain = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    diarrhoea = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    mild_fever = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    yellow_urine = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    yellowing_of_eyes = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    acute_liver_failure = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    fluid_overload = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    swelling_of_stomach = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    swelled_lymph_nodes = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    malaise = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    blurred_vision = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    phlegm = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    throat_irritation = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    redness_of_eyes = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    sinus_pressure = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    runny_nose = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    congestion = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    chest_pain = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    weakness_in_limbs = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    fast_heart_rate = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    pain_during_bowel_movements = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    pain_in_anal_region = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    bloody_stool = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    irritation_in_anus = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    neck_pain = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    dizziness = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    cramps = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    bruising = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    obesity = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    swollen_legs = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    swollen_blood_vessels = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    puffy_face_and_eyes = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    enlarged_thyroid = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect, initial='no')
    brittle_nails = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    swollen_extremeties = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    excessive_hunger = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    extra_marital_contacts = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    drying_and_tingling_lips = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    slurred_speech = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    knee_pain = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    hip_joint_pain = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    muscle_weakness = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    stiff_neck = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    swelling_joints = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    movement_stiffness = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    spinning_movements = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    loss_of_balance = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    unsteadiness = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    weakness_of_one_body_side = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    loss_of_smell = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    bladder_discomfort = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    foul_smell_of_urine = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    continuous_feel_of_urine = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    passage_of_gases = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    internal_itching = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    toxic_look_typhos = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    depression = forms.ChoiceField(choices=(("yes", "Yes"), ("no", "No")), widget=forms.RadioSelect(), initial='no')
    irritability = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    muscle_pain = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    altered_sensorium = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    red_spots_over_body = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    belly_pain = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    abnormal_menstruation = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    dischromic_patches = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    watering_from_eyes = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    increased_appetite = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    polyuria = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    family_history = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    mucoid_sputum = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    rusty_sputum = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    lack_of_concentration = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    visual_disturbances = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    receiving_blood_transfusion = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    receiving_unsterile_injections = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    coma = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    stomach_bleeding = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    distention_of_abdomen = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    history_of_alcohol_consumption = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    fluid_overload = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    blood_in_sputum = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    prominent_veins_on_calf = forms.ChoiceField(choices=(('yes', 'Yes'), ('no', 'No')), widget=forms.RadioSelect, initial='no')
    palpitations = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    painful_walking = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    pus_filled_pimples = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    blackheads = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    scurring = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    skin_peeling = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    silver_like_dusting = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    small_dents_in_nails = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    inflammatory_nails = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    blister = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    red_sore_around_nose = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    yellow_crust_ooze = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')
    prognosis = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")], widget=forms.RadioSelect, initial='no')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].initial = 'no'
    template_name = 'home.html'