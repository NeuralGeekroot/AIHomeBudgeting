import streamlit as st
from orchestrator import create_smart_home_workflow

workflow = create_smart_home_workflow()

st.title("Fully Automated Smart Home Designer")

user_input = st.text_area(
    "Describe your dream smart home:", 
    "I want a 3-bedroom smart home with security features"
)

if st.button("Design & Schedule My Smart Home"):
    with st.spinner("Automating your entire smart home setup..."):
        try:
            results = workflow.invoke({
                "user_input": user_input,
                "requirements": None,
                "architecture": None,
                "devices": None,
                "budget": None,
                "final_output": None,
                "contractors": None,
                "installation_schedule": None,
                "completion_status": []
            })
            
            st.success(f"Workflow completed! Final status: {results['completion_status'][1:-1]}")
            
            with st.expander("View Complete Workflow"):
                st.subheader("Progress History")
                for status in results["completion_status"]:
                    st.write(f"- {status}")
                
                st.subheader("Final Design")
                st.markdown(results["final_output"])
                
                st.subheader("Contractors")
                st.markdown(results["contractors"])
                
                st.subheader("Schedule")
                st.markdown(results["installation_schedule"])
                
        except Exception as e:
            st.error(f"Error in automation: {str(e)}")
            st.exception(e)